# Generated by Django 4.2.2 on 2023-11-11 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_adminprofile_bio_alter_adminprofile_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_test', models.IntegerField(default=0)),
                ('second_test', models.IntegerField(default=0)),
                ('exam', models.IntegerField(default=0)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.grade')),
            ],
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='bio',
            field=models.TextField(default='Student @ the school portal.', verbose_name='Biography'),
        ),
        migrations.AlterField(
            model_name='adminprofile',
            name='bio',
            field=models.TextField(default='Site admin @ the school portal.', verbose_name='Biography'),
        ),
        migrations.AlterField(
            model_name='adminprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/admin_profiles'),
        ),
        migrations.AlterField(
            model_name='adminprofile',
            name='position',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/student_profiles'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='subjects',
            field=models.ManyToManyField(related_name='offering_students', to='main.subject'),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='bio',
            field=models.TextField(default='Teacher @ the school portal.', null=True, verbose_name='Biography'),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/teacher_profiles'),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='subject_specializations',
            field=models.ManyToManyField(related_name='specialized_teachers', to='main.subject'),
        ),
        migrations.AlterField(
            model_name='termreport',
            name='remark',
            field=models.CharField(default='Awaiting remark...', max_length=200),
        ),
        migrations.DeleteModel(
            name='Result',
        ),
        migrations.AddField(
            model_name='subjectresult',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_results', to='main.studentprofile'),
        ),
        migrations.AddField(
            model_name='subjectresult',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_scores', to='main.subject'),
        ),
        migrations.AddField(
            model_name='subjectresult',
            name='term_report',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='results', to='main.termreport'),
        ),
    ]
