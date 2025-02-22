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
# Generated by Django 3.2 on 2021-08-17 08:02

from django.db import migrations, models

data = [
    {
        'name': 'object config issue',
        'template': {
            'message': '${source} has an issue with its config',
            'placeholder': {
                'source': {'type': 'adcm_entity'},
            },
        },
    },
    {
        'name': 'required service issue',
        'template': {
            'message': '${source} has an issue with required service',
            'placeholder': {
                'source': {'type': 'adcm_entity'},
            },
        },
    },
    {
        'name': 'required import issue',
        'template': {
            'message': '${source} has an issue with required import',
            'placeholder': {
                'source': {'type': 'adcm_entity'},
            },
        },
    },
    {
        'name': 'host component issue',
        'template': {
            'message': '${source} has an issue with host-component mapping',
            'placeholder': {
                'source': {'type': 'adcm_entity'},
            },
        },
    },
]


def insert_message_templates(apps, schema_editor):
    MessageTemplate = apps.get_model('cm', 'MessageTemplate')
    MessageTemplate.objects.bulk_create([MessageTemplate(**kwargs) for kwargs in data])


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0072_multi_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adcm',
            name='issue',
        ),
        migrations.RemoveField(
            model_name='cluster',
            name='issue',
        ),
        migrations.RemoveField(
            model_name='clusterobject',
            name='issue',
        ),
        migrations.RemoveField(
            model_name='host',
            name='issue',
        ),
        migrations.RemoveField(
            model_name='hostprovider',
            name='issue',
        ),
        migrations.RemoveField(
            model_name='servicecomponent',
            name='issue',
        ),
        migrations.AddField(
            model_name='concernitem',
            name='blocking',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='concernitem',
            name='type',
            field=models.CharField(
                choices=[('lock', 'lock'), ('issue', 'issue'), ('flag', 'flag')],
                default='lock',
                max_length=8,
            ),
        ),
        migrations.AlterField(
            model_name='concernitem',
            name='name',
            field=models.CharField(max_length=160, null=True, unique=True),
        ),
        migrations.RunPython(insert_message_templates),
    ]
