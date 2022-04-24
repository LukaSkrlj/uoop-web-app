from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import User
# Create your models here.


# class CustomAccountManager(BaseUserManager):

#     def create_superuser(self, email, password, **other_fields):

#         return self.create_user(email, password, **other_fields)

#     def create_user(self, email, password, **other_fields):

#         if not email:
#             raise ValueError('You must provide an email address')

#         email = self.normalize_email(email)
#         user = self.model(email=email, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user


# class NewUser(AbstractBaseUser, PermissionsMixin):

#     email = models.EmailField('email address', unique=True)
#     user_name = models.CharField(max_length=150, unique=True)
#     courses = models.ManyToManyField("Course")

#     USERNAME_FIELD = 'email'

#     def __str__(self):
#         return self.user_name


class Student(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    courses = models.ManyToManyField("Course")

    def __str__(self):
        return self.firstName + self.lastName


class Course(models.Model):
    title = models.CharField(max_length=50)
    shortTitle = models.CharField(max_length=5, unique=True)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    students = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title


class Test(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()

    def __str__(self):
        return self.title


class Assignment(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=10000)
    test = models.ForeignKey(
        "Test", on_delete=models.SET_NULL, null=True, blank=True)
    percentage = models.PositiveSmallIntegerField(default=0)
    inputDescription = models.TextField(max_length=10000, default='')
    outputDescription = models.TextField(max_length=10000, default='')
    isSolutionVisible = models.BooleanField(default=False)
    answer = models.TextField(max_length=10000, null=True, blank=True)
    solution = models.TextField(max_length=10000)
    tags = models.ManyToManyField("Tag")


class TestCase(models.Model):
    assignment = models.ForeignKey(
        "Assignment", on_delete=models.CASCADE, null=True, blank=True)
    hint = models.CharField(max_length=255, null=True, blank=True)
    input = models.TextField(max_length=10000)
    output = models.TextField(max_length=10000)
    memory = models.PositiveSmallIntegerField()
    time = models.PositiveSmallIntegerField(default=30)
    isVisible = models.BooleanField(default=False)

    def __str__(self):
        return self.assignment.title + ' test case'


class Tag(models.Model):
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class StudentAssignment(models.Model):
    assignment = models.ForeignKey(
        "Assignment", on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE, null=True
    )
    jar = models.FileField()


class Snippet(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )

class Quiz(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey("Course", on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=300, null=True)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    questionNum = models.IntegerField(default=0)
    students = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.CharField(max_length=50)
    quiz = models.ForeignKey("Quiz", on_delete=models.CASCADE, null=True)
    points = models.IntegerField(default=0)
    picture = models.FileField()

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=50)
    question = models.ForeignKey("Question", on_delete=models.CASCADE, null=True)
    true = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class StudentAnswer(models.Model):
    question = models.ManyToManyField("Question")
    answer = models.ManyToManyField("Answer")
    students = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.text