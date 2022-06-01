# Generated by Django 4.0.4 on 2022-05-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_studentanswer_students_studentanswer_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentanswer',
            name='answer',
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='answer',
            field=models.ManyToManyField(blank=True, to='app.answer'),
        ),
        migrations.RemoveField(
            model_name='studentanswer',
            name='question',
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='question',
            field=models.ManyToManyField(blank=True, to='app.question'),
        ),
    ]
