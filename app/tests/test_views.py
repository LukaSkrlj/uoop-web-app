from cms.test_utils.testcases import CMSTestCase
from django.test.utils import override_settings
from cgitb import text
from datetime import datetime
from mimetypes import init
from multiprocessing import context
from django.core.files import File
from turtle import title
from MySQLdb import string_literal
from django.test import Client, TestCase
from app.models import Assignment, Course, NewUser, Quiz, Snippet, Test, UserAssignment, TestCase as TC
from django.core.files.uploadedfile import SimpleUploadedFile
import mock
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# MOCK JAR FILE
java_mock = mock.MagicMock(spec=File)
java_mock.name = 'test.jar'
#


@override_settings(ROOT_URLCONF='app.tests.urls')
class ViewsTestCase(CMSTestCase):

    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://localhost:8000/app/home/')
        self.assertEqual(response.status_code, 200)

    def test_simple_get(self):
        self.client = Client()
        response = self.client.get("http://localhost:8000/app/simple/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')

    def test_simple_post(self):
        response = self.client.post("http://localhost:8000/app/simple/")
        self.assertTemplateUsed(response, 'form.html')

    def test_course_get(self):
        course = Course.objects.create(
            title="test", id=69, endDate=datetime(2015, 10, 9), startDate=datetime(2015, 10, 9))
        test = Test.objects.create(
            course_id=course.id, title="test", startDate=datetime(2015, 10, 9), endDate=datetime(2015, 10, 9))
        quiz = Quiz.objects.create(
            title="test", course_id=course.id, endDate=datetime(2015, 10, 9), startDate=datetime(2015, 10, 9))

        response = self.client.get("http://localhost:8000/app/course/69/")
        self.assertTemplateUsed(response, 'course.html')

    def test_test_get(self):
        course = Course.objects.create(
            title="test", id=59, endDate=datetime(2015, 10, 9), startDate=datetime(2015, 10, 9))
        test = Test.objects.create(
            id=69, course_id=course.id, title="test", startDate=datetime(2015, 10, 9), endDate=datetime(2015, 10, 10))
        assignment = Assignment.objects.create(title="test", test=test)
        response = self.client.get("http://localhost:8000/app/test/69/")
        self.assertTemplateUsed(response, 'test.html')

    def test_assignment_get(self):
        course = Course.objects.create(
            title="test", id=59, endDate=datetime(2015, 10, 9), startDate=datetime(2015, 10, 9))
        test = Test.objects.create(
            id=69, course_id=course.id, title="test", startDate=datetime(2015, 10, 9), endDate=datetime(2015, 10, 9))
        assignment = Assignment.objects.create(title="test", test=test, id=5)
        testCase = TC.objects.create(
            assignment=assignment, input="test", output="test", memoryLimit=10)
        user = NewUser.objects.create(
            email='test@test.com', password='test')
        userAssignment = UserAssignment.objects.create(
            id=5, assignment=assignment, newuser=user, jar=SimpleUploadedFile(java_mock._extract_mock_name(), b"java"))
        response = self.client.get("http://localhost:8000/app/assignment/5/")
        self.assertTemplateUsed(response, 'assignment.html')

    def test_assignment_post(self):
        course = Course.objects.create(
            title="test", id=59, endDate=datetime(2015, 10, 9), startDate=datetime(2015, 10, 9))
        test = Test.objects.create(
            id=69, course_id=course.id, title="test", startDate=datetime(2015, 10, 9), endDate=datetime(2015, 10, 9))
        assignment = Assignment.objects.create(
            title="test", test=test, id=5)
        testCase = TC.objects.create(
            assignment=assignment, input="test", output="test", memoryLimit=10)
        user = NewUser.objects.create(
            email='test@test.com', password='test')
        userAssignment = UserAssignment.objects.create(
            id=5, assignment=assignment, newuser=user, jar=SimpleUploadedFile(java_mock._extract_mock_name(), b"java"))
        response = self.client.get("http://localhost:8000/app/assignment/5/")
        self.assertTemplateUsed(response, 'assignment.html')

    def test_input(self):
        course = Course.objects.create(
            title="test", id=59, endDate=datetime(2015, 10, 9), startDate=datetime(2015, 10, 9))
        test = Test.objects.create(
            id=69, course=course, title="test", startDate=datetime(2015, 10, 9), endDate=datetime(2015, 10, 9))
        assignment = Assignment.objects.create(
            title="test", test=test, id=5)
        input = TC.objects.create(
            assignment=assignment, input="test", output="test", memoryLimit=10)
        context = {}
        context["txt"] = input
        response = self.client.post(
            "http://localhost:8000/app/input/5/", context)
        pass

    def test_logout_user(self):
        response = self.client.post(
            "http://localhost:8000/app/logout_user/")
        self.assertRedirects(response, "/app/home/")

    def test_osustavu(self):
        response = self.client.get(
            "http://localhost:8000/app/osustavu/")
        self.assertTemplateUsed(response, 'osustavu.html')

    def automatiziranaprovjera(self):
        response = self.client.get(
            "http://localhost:8000/automatiziranaprovjera/")
        self.assertTemplateUsed(response, 'automatiziranaprovjera.html')
