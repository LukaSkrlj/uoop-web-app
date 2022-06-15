# Generated by Django 3.1.14 on 2022-06-13 17:07

import cms.models.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('true', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=10000)),
                ('percentage', models.PositiveSmallIntegerField(default=0)),
                ('inputDescription', models.TextField(max_length=10000)),
                ('outputDescription', models.TextField(max_length=10000)),
                ('isSolutionVisible', models.BooleanField(default=False)),
                ('answer', models.TextField(blank=True, max_length=10000, null=True)),
                ('assignmentTemplate', models.FileField(null=True, upload_to='assignment_templates', validators=[django.core.validators.FileExtensionValidator(['jar'])])),
                ('solutionFile', models.FileField(null=True, upload_to='assignment_solutions', validators=[django.core.validators.FileExtensionValidator(['jar'])])),
                ('solution', models.TextField(max_length=10000)),
                ('test_class', models.CharField(default='JunitTest', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('shortTitle', models.CharField(max_length=5, unique=True)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('newusers', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300, null=True)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('points', models.FloatField(default=0)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('students', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hint', models.CharField(blank=True, max_length=255, null=True)),
                ('input', models.TextField(max_length=10000)),
                ('output', models.TextField(max_length=10000)),
                ('memoryLimit', models.PositiveSmallIntegerField()),
                ('timeLimit', models.PositiveSmallIntegerField(default=30)),
                ('isVisible', models.BooleanField(default=False)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.assignment')),
            ],
        ),
        migrations.CreateModel(
            name='UserAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jar', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['jar'])])),
                ('percentage', models.PositiveSmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assignment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.assignment')),
                ('newuser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserTestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField(default=False)),
                ('memory', models.PositiveSmallIntegerField(null=True)),
                ('time', models.PositiveSmallIntegerField(null=True)),
                ('error', models.TextField(null=True)),
                ('output_label', models.CharField(max_length=200, null=True)),
                ('user_output', models.TextField(default='', max_length=10000)),
                ('testcase', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.testcase')),
                ('userassignment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.userassignment')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
            ],
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
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.FloatField(default=0)),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.answer')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.question')),
                ('studentQuiz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.studentquiz')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='app.quiz'),
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_placeholder', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='placeholder_name', to='cms.placeholder')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.test'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='app.question'),
        ),
    ]
