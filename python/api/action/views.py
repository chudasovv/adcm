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

from django.contrib.contenttypes.models import ContentType
from guardian.mixins import PermissionListMixin
from rest_framework import permissions
from rest_framework.response import Response

from api.base_view import GenericUIView
from api.job.serializers import RunTaskSerializer
from api.utils import (
    ActionFilter,
    AdcmFilterBackend,
    create,
    filter_actions,
    permission_denied,
    get_object_for_user,
)
from cm.job import get_host_object
from cm.models import (
    Host,
    Action,
    TaskLog,
    HostComponent,
    get_model_by_type,
)
from rbac.viewsets import DjangoOnlyObjectPermissions
from . import serializers


def get_object_type_id(**kwargs):
    object_type = kwargs.get('object_type')
    object_id = kwargs.get(f'{object_type}_id')
    action_id = kwargs.get('action_id', None)
    return object_type, object_id, action_id


def get_obj(**kwargs):
    object_type, object_id, action_id = get_object_type_id(**kwargs)
    model = get_model_by_type(object_type)
    obj = model.obj.get(id=object_id)
    return obj, action_id


class ActionList(PermissionListMixin, GenericUIView):
    queryset = Action.objects.all()
    serializer_class = serializers.ActionSerializer
    serializer_class_ui = serializers.ActionUISerializer
    filterset_class = ActionFilter
    filterset_fields = ('name', 'button', 'button_is_null')
    filter_backends = (AdcmFilterBackend,)
    permission_required = ['cm.view_action']

    def get(self, request, *args, **kwargs):  # pylint: disable=too-many-locals
        """
        List all actions of a specified object
        """
        if kwargs['object_type'] == 'host':
            host, _ = get_obj(object_type='host', host_id=kwargs['host_id'])
            actions = set(
                filter_actions(
                    host, self.filter_queryset(self.get_queryset().filter(prototype=host.prototype))
                )
            )
            obj = host
            objects = {'host': host}
            hcs = HostComponent.objects.filter(host_id=kwargs['host_id'])
            if hcs:
                for hc in hcs:
                    cluster, _ = get_obj(object_type='cluster', cluster_id=hc.cluster_id)
                    service, _ = get_obj(object_type='service', service_id=hc.service_id)
                    component, _ = get_obj(object_type='component', component_id=hc.component_id)
                    for obj in [cluster, service, component]:
                        actions.update(
                            filter_actions(
                                obj,
                                self.filter_queryset(
                                    self.get_queryset().filter(
                                        prototype=obj.prototype, host_action=True
                                    )
                                ),
                            )
                        )
            else:
                if host.cluster is not None:
                    actions.update(
                        filter_actions(
                            host.cluster,
                            self.filter_queryset(
                                self.get_queryset().filter(
                                    prototype=host.cluster.prototype, host_action=True
                                )
                            ),
                        )
                    )
        else:
            obj, _ = get_obj(**kwargs)
            actions = filter_actions(
                obj,
                self.filter_queryset(
                    self.get_queryset().filter(prototype=obj.prototype, host_action=False)
                ),
            )
            objects = {obj.prototype.type: obj}
        serializer = self.get_serializer(
            actions, many=True, context={'request': request, 'objects': objects, 'obj': obj}
        )
        return Response(serializer.data)


class ActionDetail(PermissionListMixin, GenericUIView):
    queryset = Action.objects.all()
    serializer_class = serializers.ActionDetailSerializer
    serializer_class_ui = serializers.ActionUISerializer
    permission_classes = (DjangoOnlyObjectPermissions,)
    permission_required = ['cm.view_action']

    def get(self, request, *args, **kwargs):
        """
        Show specified action
        """
        object_type, object_id, action_id = get_object_type_id(**kwargs)
        model = get_model_by_type(object_type)
        ct = ContentType.objects.get_for_model(model)
        obj = get_object_for_user(
            request.user, f'{ct.app_label}.view_{ct.model}', model, id=object_id
        )
        # TODO: we can access not only the actions of this object
        action = get_object_for_user(request.user, 'cm.view_action', Action, id=action_id)
        if isinstance(obj, Host) and action.host_action:
            objects = {'host': obj}
        else:
            objects = {action.prototype.type: obj}
        serializer = self.get_serializer(
            action, context={'request': request, 'objects': objects, 'obj': obj}
        )
        return Response(serializer.data)


class RunTask(GenericUIView):
    queryset = TaskLog.objects.all()
    serializer_class = RunTaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def has_action_perm(self, action, obj):
        user = self.request.user

        if user.has_perm('cm.add_task'):
            return True

        if action.host_action:
            obj = get_host_object(action, obj.cluster)

        return user.has_perm(f'cm.run_action_{action.display_name}', obj)

    def check_action_perm(self, action, obj):
        if not self.has_action_perm(action, obj):
            permission_denied()

    def post(self, request, *args, **kwargs):
        """
        Ran specified action
        """
        object_type, object_id, action_id = get_object_type_id(**kwargs)
        model = get_model_by_type(object_type)
        ct = ContentType.objects.get_for_model(model)
        obj = get_object_for_user(
            request.user, f'{ct.app_label}.view_{ct.model}', model, id=object_id
        )
        action = get_object_for_user(request.user, 'cm.view_action', Action, id=action_id)
        self.check_action_perm(action, obj)
        serializer = self.get_serializer(data=request.data)
        return create(serializer, action=action, task_object=obj)
