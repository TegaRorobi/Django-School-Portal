# Generated by Django 4.2.1 on 2023-07-22 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='label',
            field=models.CharField(choices=[('Kindergarten 1', 'Kindergarten 1'), ('Kindergarten 2', 'Kindergarten 2'), ('Nursery 1', 'Nursery 1'), ('Nursery 2', 'Nursery 2'), ('Primary 1', 'Primary 1'), ('Primary 2', 'Primary 2'), ('Primary 3', 'Primary 3'), ('Primary 4', 'Primary 4'), ('Primary 5', 'Primary 5')], max_length=15),
        ),
    ]
