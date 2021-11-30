# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""User view sets"""

from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers

from rbac import models
from rbac.services import user as user_services
from rbac.viewsets import ModelPermViewSet, DjangoModelPerm


class UserPermissions(DjangoModelPerm):
    """Special permission class for User to allow user change own properties"""

    def has_permission(self, request, view):
        if not all((request.user, request.user.is_active, request.user.is_authenticated)):
            return False
        if request.user.is_superuser:
            return True
        if view.action not in ('retrieve', 'update', 'partial_update'):
            return False
        return int(view.kwargs.get('pk', 0)) == request.user.pk


class PasswordField(serializers.CharField):
    """Text field with content masking for passwords"""

    def to_representation(self, value):
        return user_services.PW_MASK


class GroupSerializer(serializers.Serializer):
    """Simple Group representation serializer"""

    id = serializers.IntegerField()
    url = serializers.HyperlinkedIdentityField(view_name='rbac:group-detail')


class GroupUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    url = serializers.HyperlinkedIdentityField(view_name='rbac:user-detail')


class ExpandedGroupSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    """Expanded Group serializer"""

    description = serializers.CharField(source='group.description')
    user = GroupUserSerializer(many=True, source='user_set')
    url = serializers.HyperlinkedIdentityField(view_name='rbac:group-detail')

    class Meta:
        model = models.Group
        fields = ('id', 'name', 'description', 'user', 'url')
        expandable_fields = {
            'user': (
                'rbac.endpoints.user.views.UserSerializer',
                {'many': True, 'source': 'user_set'},
            )
        }


class UserSerializer(FlexFieldsSerializerMixin, serializers.Serializer):
    """User serializer"""

    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    first_name = serializers.CharField(allow_blank=True, default='')
    last_name = serializers.CharField(allow_blank=True, default='')
    email = serializers.EmailField(allow_blank=True, required=False)
    is_superuser = serializers.BooleanField(default=False)
    password = PasswordField(trim_whitespace=False)
    url = serializers.HyperlinkedIdentityField(view_name='rbac:user-detail')
    profile = serializers.JSONField(source='userprofile.profile', required=False, default='')
    groups = GroupSerializer(many=True, required=False)

    class Meta:
        expandable_fields = {'groups': (ExpandedGroupSerializer, {'many': True})}

    def update(self, instance, validated_data):
        if 'userprofile' in validated_data:
            validated_data['profile'] = validated_data.pop('userprofile')['profile']
        context_user = self.context['request'].user
        return user_services.update(instance, context_user, partial=self.partial, **validated_data)

    def create(self, validated_data):
        if 'userprofile' in validated_data:
            validated_data['profile'] = validated_data.pop('userprofile')['profile']
        return user_services.create(**validated_data)


class UserViewSet(ModelPermViewSet):  # pylint: disable=too-many-ancestors
    """User view set"""

    queryset = models.User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_superuser']
    ordering_fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_superuser']
    permission_classes = (UserPermissions,)
