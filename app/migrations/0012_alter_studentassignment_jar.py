# Generated by Django 3.2.9 on 2022-02-25 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_studentassignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentassignment',
            name='jar',
            field=models.FileField(upload_to=''),
        ),
    ]
