# Generated by Django 4.2.2 on 2023-11-14 13:47

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_studenttermreport_alter_subjectresult_term_report_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-date_created']},
        ),
        migrations.RenameField(
            model_name='message',
            old_name='timestamp',
            new_name='date_created',
        ),
        migrations.AddField(
            model_name='grade',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grade',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='message',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='term',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 11, 14, 13, 47, 5, 51275, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='term',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
