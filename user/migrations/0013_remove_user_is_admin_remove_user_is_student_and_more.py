# Generated by Django 5.0 on 2024-01-06 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_user_managers_alter_user_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_teacher',
        ),
    ]
