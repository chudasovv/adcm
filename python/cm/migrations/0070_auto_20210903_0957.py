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

# Generated by Django 3.2.6 on 2021-09-03 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0069_auto_20210607_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='prototype',
            name='config_group_customized',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stageprototype',
            name='config_group_customized',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='prototypeconfig',
            name='group_customization',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='stageprototypeconfig',
            name='group_customization',
            field=models.BooleanField(null=True),
        ),
    ]
