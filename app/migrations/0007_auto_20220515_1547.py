# Generated by Django 3.1.14 on 2022-05-15 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220515_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertestcase',
            name='userassignment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.userassignment'),
        ),
    ]
