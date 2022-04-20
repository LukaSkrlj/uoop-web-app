from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import FileExtensionValidator
from django.db import models


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
    first_name = models.CharField(max_length=150)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


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
    students = models.ManyToManyField(NewUser, blank=True)

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
    tags = models.ManyToManyField("Tag")
    assignmentTemplate = models.FileField(validators=[FileExtensionValidator(['jar'])], upload_to='assignment_templates', null=True)
    #TODO try to read Java code from files and then solution atribute can be removed
    solutionFile = models.FileField(validators=[FileExtensionValidator(['jar'])], upload_to='assignment_solutions', null=True)
    solution = models.TextField(max_length=10000)

    def __str__(self):
        return self.title


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
        NewUser,
        on_delete=models.CASCADE, null=True
    )
    jar = models.FileField(validators=[FileExtensionValidator(['jar'])])


class Snippet(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )

#TODO improve student file management after user-assignment relation is added
# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.user.id, filename)

# class MyModel(models.Model):
#     upload = models.FileField(upload_to=user_directory_path)