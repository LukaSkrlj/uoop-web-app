# Generated by Django 3.1.14 on 2022-06-15 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='percentage',
            field=models.PositiveSmallIntegerField(blank=True, default=None, null=True),
        ),
    ]
