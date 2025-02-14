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


from django.urls import include, path

from api.component.views import ComponentDetailView, ComponentListView, StatusList

urlpatterns = [
    path('', ComponentListView.as_view(), name='component'),
    path(
        '<int:component_id>/',
        include(
            [
                path('', ComponentDetailView.as_view(), name='component-details'),
                path('config/', include('api.config.urls'), {'object_type': 'component'}),
                path('action/', include('api.action.urls'), {'object_type': 'component'}),
                path('status/', StatusList.as_view(), name='component-status'),
            ]
        ),
    ),
]
