# Generated by Django 3.1.14 on 2022-06-06 23:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='questionNum',
        ),
        migrations.RemoveField(
            model_name='studentanswer',
            name='students',
        ),
        migrations.AddField(
            model_name='quiz',
            name='points',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='points',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='usertestcase',
            name='user_output',
            field=models.TextField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.RemoveField(
            model_name='studentanswer',
            name='answer',
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.answer'),
        ),
        migrations.RemoveField(
            model_name='studentanswer',
            name='question',
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.question'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='test',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userassignment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='StudentQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.FloatField(default=0)),
                ('percentage', models.FloatField(default=0)),
                ('quiz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.quiz')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='studentQuiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.studentquiz'),
        ),
    ]
