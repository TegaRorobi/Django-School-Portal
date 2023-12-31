# Generated by Django 4.2.5 on 2023-09-09 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminprofile',
            name='id',
        ),
        migrations.AlterField(
            model_name='adminprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='admin_profile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
