from datetime import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model

from app.models import Assignment, Course, NewUser, Quiz, Tag, Test, UserAssignment
from app.views import assignment


class ModelsTestCase(TestCase):

    # Regular user/student creating test
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='test@test.com', password='test')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="test")

    # Superuser creating test
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email='test@test.com', password='test')
        self.assertEqual(admin_user.email, 'test@test.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)

    # Test User self
    def test_str_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='test@test.com', password='test')
        self.assertEqual(str(user), user.email)

    # Test Course self
    def test_str_course(self):
        course = Course.objects.create(
            title="test", endDate=datetime.now(), startDate=datetime.now())
        self.assertEqual(str(course), course.title)

    # Test Test self
    def test_str_test(self):
        course = Course.objects.create(
            id=1, endDate=datetime.now(), startDate=datetime.now())
        test = Test.objects.create(
            course_id=course.id, title="test", startDate=datetime.now(), endDate=datetime.now())
        self.assertEqual(str(test), test.title)

    # Test Assignment self
    def test_str_assignment(self):
        assignment = Assignment.objects.create(title="test")
        self.assertEqual(str(assignment), assignment.title)

    # Test Tag self
    def test_str_tag(self):
        tag = Tag.objects.create(name="test")
        self.assertEqual(str(tag), tag.name)

    # Test Quiz self
    def test_str_quiz(self):
        course = Course.objects.create(
            id=1, endDate=datetime.now(), startDate=datetime.now())
        quiz = Quiz.objects.create(
            title="test", course_id=course.id, endDate=datetime.now(), startDate=datetime.now())
        self.assertEqual(str(quiz), quiz.title)
