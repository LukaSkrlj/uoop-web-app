# Generated by Django 3.1.14 on 2022-04-22 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20220422_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='description',
        ),
        migrations.RemoveField(
            model_name='question',
            name='idQuestion',
        ),
        migrations.RemoveField(
            model_name='question',
            name='solution',
        ),
    ]
