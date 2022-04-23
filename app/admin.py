from django.contrib import admin

# Register your models here.

from app.models import Course, Test, Assignment, TestCase, Tag, StudentAssignment, Quiz, Question, Answer

admin.site.register(Course)
admin.site.register(Test)
admin.site.register(TestCase)
admin.site.register(Assignment)
admin.site.register(Tag)
admin.site.register(StudentAssignment)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
