# Generated by Django 4.2.2 on 2023-11-15 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_message_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectresult',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='subjectresult',
            name='student',
        ),
        migrations.AlterField(
            model_name='subjectresult',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_results', to='main.subject'),
        ),
    ]