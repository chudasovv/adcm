# Generated by Django 3.2.11 on 2022-01-30 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0083_add_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='_venv',
            field=models.CharField(db_column='venv', default='default', max_length=160),
        ),
        migrations.AddField(
            model_name='prototype',
            name='venv',
            field=models.CharField(default='default', max_length=160),
        ),
        migrations.AddField(
            model_name='stageaction',
            name='_venv',
            field=models.CharField(db_column='venv', default='default', max_length=160),
        ),
        migrations.AddField(
            model_name='stageprototype',
            name='venv',
            field=models.CharField(default='default', max_length=160),
        ),
    ]
