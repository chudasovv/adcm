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

# Generated by Django 3.0.5 on 2020-04-03 08:25

# pylint: disable=line-too-long

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0050_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupCheckLog',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('job_id', models.PositiveIntegerField(default=0)),
                ('title', models.TextField()),
                ('message', models.TextField(blank=True, null=True)),
                ('result', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='checklog',
            name='group',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='cm.GroupCheckLog',
            ),
        ),
    ]
