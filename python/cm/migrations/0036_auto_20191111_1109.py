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
# Generated by Django 2.2.4 on 2019-11-11 11:09
# pylint: disable=line-too-long

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0035_auto_20191031_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundle',
            name='license',
            field=models.CharField(
                choices=[
                    ('absent', 'absent'),
                    ('accepted', 'accepted'),
                    ('unaccepted', 'unaccepted'),
                ],
                default='absent',
                max_length=16,
            ),
        ),
        migrations.AddField(
            model_name='bundle',
            name='license_hash',
            field=models.CharField(default=None, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='bundle',
            name='license_path',
            field=models.CharField(default=None, max_length=160, null=True),
        ),
        migrations.AddField(
            model_name='stageprototype',
            name='license_hash',
            field=models.CharField(default=None, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='stageprototype',
            name='license_path',
            field=models.CharField(default=None, max_length=160, null=True),
        ),
    ]
