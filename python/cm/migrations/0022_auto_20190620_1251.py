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
# Generated by Django 2.2.1 on 2019-06-20 12:51
# pylint: disable=line-too-long


import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0021_auto_20190607_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='prototype',
            name='shared',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stageprototype',
            name='shared',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='clusterbind',
            name='source_cluster',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='source_cluster',
                to='cm.Cluster',
            ),
        ),
        migrations.AlterField(
            model_name='clusterbind',
            name='source_service',
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='source_service',
                to='cm.ClusterObject',
            ),
        ),
    ]
