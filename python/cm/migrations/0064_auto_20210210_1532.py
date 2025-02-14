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
# Generated by Django 3.1.1 on 2021-02-10 15:32
# pylint: disable=line-too-long

from django.db import migrations, models

FIELDS = [
    ('string', 'string'),
    ('text', 'text'),
    ('password', 'password'),
    ('secrettext', 'secrettext'),
    ('json', 'json'),
    ('integer', 'integer'),
    ('float', 'float'),
    ('option', 'option'),
    ('variant', 'variant'),
    ('boolean', 'boolean'),
    ('file', 'file'),
    ('list', 'list'),
    ('map', 'map'),
    ('structure', 'structure'),
    ('group', 'group'),
]


class Migration(migrations.Migration):
    dependencies = [
        ('cm', '0063_tasklog_verbose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prototypeconfig',
            name='type',
            field=models.CharField(choices=FIELDS, max_length=16),
        ),
        migrations.AlterField(
            model_name='stageprototypeconfig',
            name='type',
            field=models.CharField(choices=FIELDS, max_length=16),
        ),
    ]
