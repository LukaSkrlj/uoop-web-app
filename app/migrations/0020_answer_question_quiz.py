# Generated by Django 3.1.14 on 2022-04-22 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_merge_20220407_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('questionNum', models.IntegerField(default=0)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.course')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=10000)),
                ('solution', models.TextField(max_length=10000)),
                ('idQuestion', models.IntegerField(default=0)),
                ('quiz', models.ManyToManyField(to='app.Quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('answer', models.TextField(blank=True, max_length=10000, null=True)),
                ('true', models.BooleanField(default=False)),
                ('test', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.question')),
            ],
        ),
    ]
