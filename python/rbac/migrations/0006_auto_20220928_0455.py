# Generated by Django 3.2.15 on 2022-09-28 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0005_rbac_group_unique_display_name_type_constraint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='display_name',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=1000),
        ),
    ]
