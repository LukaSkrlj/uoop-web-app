from datetime import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from app.models import Assignment, Course, Quiz, Tag, Test, UserAssignment
from app.views import assignment


class ModelsTestCase(TestCase):

    # Regular user/student creating test
    def test_create_user(self):
        user = User.objects.create_user(
            username='test', password='test')
        self.assertEqual(user.username, 'test')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    # Superuser creating test
    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            username='test', password='test')
        self.assertEqual(admin_user.username, 'test')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    # Test User self
    def test_str_user(self):
        user = User.objects.create_user(username='test', password='test')
        self.assertEqual(str(user), user.username)

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
