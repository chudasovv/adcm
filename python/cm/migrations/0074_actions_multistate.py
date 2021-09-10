# Generated by Django 3.2 on 2021-09-14 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0073_issues_refactoring'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='multi_state_available',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='action',
            name='multi_state_on_fail_set',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='action',
            name='multi_state_on_fail_unset',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='action',
            name='multi_state_on_success_set',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='action',
            name='multi_state_on_success_unset',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='action',
            name='multi_state_unavailable',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='action',
            name='state_unavailable',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='stageaction',
            name='multi_state_available',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='stageaction',
            name='multi_state_on_fail_set',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='stageaction',
            name='multi_state_on_fail_unset',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='stageaction',
            name='multi_state_on_success_set',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='stageaction',
            name='multi_state_on_success_unset',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='stageaction',
            name='multi_state_unavailable',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='stageaction',
            name='state_unavailable',
            field=models.JSONField(default=list),
        ),
    ]
