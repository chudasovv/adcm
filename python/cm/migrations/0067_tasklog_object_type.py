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
# Generated by Django 3.1.2 on 2021-06-04 15:37

import django.db.models.deletion
from django.db import migrations, models


def fix_tasklog(apps, schema_editor):
    TaskLog = apps.get_model('cm', 'TaskLog')
    ServiceComponent = apps.get_model('cm', 'ServiceComponent')
    ClusterObject = apps.get_model('cm', 'ClusterObject')
    Host = apps.get_model('cm', 'Host')
    Cluster = apps.get_model('cm', 'Cluster')
    HostProvider = apps.get_model('cm', 'HostProvider')
    ADCM = apps.get_model('cm', 'ADCM')

    ContentType = apps.get_model('contenttypes', 'ContentType')
    cash = {}

    def get_content(context):
        content = {
            'component': 'servicecomponent',
            'service': 'clusterobject',
            'host': 'host',
            'provider': 'hostprovider',
            'cluster': 'cluster',
            'adcm': 'adcm',
        }
        if context not in cash:
            cash[context] = ContentType.objects.get(app_label='cm', model=content[context])
        return cash[context]

    def get_task_obj(action, obj_id):
        if action is None:
            return None

        def get_obj_safe(model, obj_id):
            try:
                return model.objects.get(id=obj_id)
            except model.DoesNotExist:
                return None

        context = action.prototype.type
        if context == 'component':
            obj = get_obj_safe(ServiceComponent, obj_id)
        elif context == 'service':
            obj = get_obj_safe(ClusterObject, obj_id)
        elif context == 'host':
            obj = get_obj_safe(Host, obj_id)
        elif context == 'cluster':
            obj = get_obj_safe(Cluster, obj_id)
        elif context == 'provider':
            obj = get_obj_safe(HostProvider, obj_id)
        elif context == 'adcm':
            obj = get_obj_safe(ADCM, obj_id)
        else:
            return None
        return obj

    for task in TaskLog.objects.all():
        obj = get_task_obj(task.action, task.object_id)
        if obj:
            task.object_type = get_content(task.action.prototype.type)
            task.save()


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('cm', '0066_auto_20210427_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklog',
            name='object_type',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='contenttypes.contenttype',
            ),
        ),
        migrations.RunPython(fix_tasklog),
    ]
