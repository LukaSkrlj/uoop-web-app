# Generated by Django 4.0.4 on 2022-05-16 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_studentanswer_answer_studentanswer_answer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentanswer',
            name='students',
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
    ]
