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
# Generated by Django 2.1.7 on 2019-03-14 13:21
# pylint: disable=line-too-long

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0018_auto_20190220_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='monitoring',
            field=models.CharField(
                choices=[('active', 'active'), ('passive', 'passive')],
                default='active',
                max_length=16,
            ),
        ),
        migrations.AddField(
            model_name='prototype',
            name='monitoring',
            field=models.CharField(
                choices=[('active', 'active'), ('passive', 'passive')],
                default='active',
                max_length=16,
            ),
        ),
        migrations.AddField(
            model_name='stagecomponent',
            name='monitoring',
            field=models.CharField(
                choices=[('active', 'active'), ('passive', 'passive')],
                default='active',
                max_length=16,
            ),
        ),
        migrations.AddField(
            model_name='stageprototype',
            name='monitoring',
            field=models.CharField(
                choices=[('active', 'active'), ('passive', 'passive')],
                default='active',
                max_length=16,
            ),
        ),
    ]
