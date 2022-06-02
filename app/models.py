from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import FileExtensionValidator
from django.db import models

from app.constants import SOLUTIONS_FOLDER, TEMPLATES_FOLDER


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    courses = models.ManyToManyField("Course")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Course(models.Model):
    title = models.CharField(max_length=50)
    shortTitle = models.CharField(max_length=5, unique=True)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    newusers = models.ManyToManyField(NewUser, blank=True)

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
    inputDescription = models.TextField(max_length=10000)
    outputDescription = models.TextField(max_length=10000)
    isSolutionVisible = models.BooleanField(default=False)
    answer = models.TextField(max_length=10000, null=True, blank=True)
    tags = models.ManyToManyField("Tag")
    assignmentTemplate = models.FileField(validators=[FileExtensionValidator(
        ['jar'])], upload_to='assignment_templates', null=True)
    # TODO try to read Java code from files and then solution atribute can be removed
    solutionFile = models.FileField(validators=[FileExtensionValidator(
        ['jar'])], upload_to='assignment_solutions', null=True)
    solution = models.TextField(max_length=10000)

    def __str__(self):
        return self.title


class TestCase(models.Model):
    assignment = models.ForeignKey(
        "Assignment", on_delete=models.CASCADE)
    hint = models.CharField(max_length=255, null=True, blank=True)
    input = models.TextField(max_length=10000)
    output = models.TextField(max_length=10000)
    memoryLimit = models.PositiveSmallIntegerField()
    timeLimit = models.PositiveSmallIntegerField(default=30)
    isVisible = models.BooleanField(default=False)

    def __str__(self):
        return self.assignment.title + ' test case'


class Tag(models.Model):
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class UserAssignment(models.Model):
    assignment = models.ForeignKey(
        "Assignment", on_delete=models.CASCADE, null=True)
    newuser = models.ForeignKey(
        "NewUser", on_delete=models.CASCADE, null=True
    )
    # Jar file that user uploads/downloads for each assignment
    jar = models.FileField(validators=[FileExtensionValidator(['jar'])])
    # Percantage of completed assignment
    percentage = models.PositiveSmallIntegerField(default=0)
    # Automatically set the field to now when the object is first created.
    # Note that the current date is always used; it’s not just a default value that you can override.
    created_at = models.DateTimeField(auto_now_add=True)
    # Automatically set the field to now every time the object is saved.
    # Note that the current date is always used; it’s not just a default value that you can override.
    updated_at = models.DateTimeField(auto_now=True)


class Snippet(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )


class UserTestCase(models.Model):
    is_correct = models.BooleanField(default=False)
    memory = models.PositiveSmallIntegerField(null=True)
    time = models.PositiveSmallIntegerField(null=True)
    error = models.TextField(null=True)
    output_label = models.CharField(max_length=200, null=True)
    userassignment = models.ForeignKey(
        'UserAssignment', on_delete=models.CASCADE, null=True
    )
    testcase = models.ForeignKey(
        'TestCase', on_delete=models.CASCADE, null=True
    )

    
class Quiz(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey("Course", on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=300, null=True)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    students = models.ManyToManyField(NewUser, blank=True)

    def __str__(self):
        return self.title
    
    def __getDate__(self):
        return self.endDate


class Question(models.Model):
    text = models.CharField(max_length=50)
    quiz = models.ForeignKey("Quiz", on_delete=models.CASCADE, null=True,  related_name='question')
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.text
    

class Answer(models.Model):
    text = models.CharField(max_length=50)
    question = models.ForeignKey("Question", on_delete=models.CASCADE, null=True,  related_name='answer')
    true = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class StudentQuiz(models.Model): #model that stores students name, name of the quiz and percentage he scored
    quiz = models.ForeignKey("Quiz", on_delete=models.CASCADE, null=True)
    student = models.ForeignKey("NewUser", on_delete=models.CASCADE, null=True)
    percentage = models.IntegerField(default=0)
    def __str__(self):  #naming object in db
       if self.quiz and self.student.first_name and self.student.lastName:
           return self.quiz.title + '-' + self.student.first_name + ' ' + self.student.lastName
       if self.quiz and self.student.email:
            return self.quiz.title + '-' + self.student.email
       return "unknown"


class StudentAnswer(models.Model): #model that stores students answer to a question
    studentQuiz = models.ForeignKey("StudentQuiz", on_delete=models.CASCADE, null=True)
    question = models.ForeignKey("Question", on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey("Answer", on_delete=models.CASCADE, null=True)
    def __str__(self):  #naming object in db
        if self.studentQuiz.quiz.title and self.question.text:
                return self.studentQuiz.quiz.title + '-' + self.question.text
        if self.studentQuiz.title and not self.question.text:
                return self.studentQuiz.quiz.title + '-' + '?'
        return  "unknown"


#TODO improve student file management after user-assignment relation is added
# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.user.id, filename)

# class MyModel(models.Model):
#     upload = models.FileField(upload_to=user_directory_path)
