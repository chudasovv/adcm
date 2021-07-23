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
# Generated by Django 3.2 on 2021-06-22 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0067_tasklog_object_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConcernItem',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('name', models.CharField(max_length=160, null=True)),
                ('reason', models.JSONField(default=dict)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='adcm',
            name='stack',
        ),
        migrations.RemoveField(
            model_name='cluster',
            name='stack',
        ),
        migrations.RemoveField(
            model_name='clusterobject',
            name='stack',
        ),
        migrations.RemoveField(
            model_name='host',
            name='stack',
        ),
        migrations.RemoveField(
            model_name='hostprovider',
            name='stack',
        ),
        migrations.RemoveField(
            model_name='servicecomponent',
            name='stack',
        ),
        migrations.AddField(
            model_name='adcm',
            name='concern',
            field=models.ManyToManyField(
                blank=True, related_name='adcm_entities', to='cm.ConcernItem'
            ),
        ),
        migrations.AddField(
            model_name='cluster',
            name='concern',
            field=models.ManyToManyField(
                blank=True, related_name='cluster_entities', to='cm.ConcernItem'
            ),
        ),
        migrations.AddField(
            model_name='clusterobject',
            name='concern',
            field=models.ManyToManyField(
                blank=True, related_name='clusterobject_entities', to='cm.ConcernItem'
            ),
        ),
        migrations.AddField(
            model_name='host',
            name='concern',
            field=models.ManyToManyField(
                blank=True, related_name='host_entities', to='cm.ConcernItem'
            ),
        ),
        migrations.AddField(
            model_name='hostprovider',
            name='concern',
            field=models.ManyToManyField(
                blank=True, related_name='hostprovider_entities', to='cm.ConcernItem'
            ),
        ),
        migrations.AddField(
            model_name='servicecomponent',
            name='concern',
            field=models.ManyToManyField(
                blank=True, related_name='servicecomponent_entities', to='cm.ConcernItem'
            ),
        ),
        migrations.AddField(
            model_name='tasklog',
            name='lock',
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='cm.concernitem',
            ),
        ),
    ]
