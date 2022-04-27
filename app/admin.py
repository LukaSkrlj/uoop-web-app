from django.contrib import admin

# Register your models here.

from app.models import Answer, Course, NewUser, Question, Quiz, StudentAnswer, Test, Assignment, TestCase, Tag, UserAssignment, UserTestCase

admin.site.register(Course)
admin.site.register(Test)
admin.site.register(TestCase)
admin.site.register(Assignment)
admin.site.register(Tag)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(StudentAnswer)
admin.site.register(UserAssignment)
admin.site.register(NewUser)
admin.site.register(UserTestCase)
