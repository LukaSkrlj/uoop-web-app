# Generated by Django 3.1.14 on 2022-06-07 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220607_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='test_class',
            field=models.CharField(default='JunitTest', max_length=50, null=True),
        ),
    ]
