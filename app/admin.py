from django.contrib import admin

# Register your models here.

from app.models import Answer, Course, NewUser, Question, Quiz, StudentAnswer, StudentQuiz, Test, Assignment, TestCase, Tag, UserAssignment, UserTestCase

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
admin.site.register(StudentQuiz)

class StudentAnswerInline(admin.TabularInline):
    model = StudentAnswer

class StudentQuizAdmin(admin.ModelAdmin):
   inlines = [StudentAnswerInline,]

admin.site.unregister(StudentQuiz)
admin.site.register(StudentQuiz,StudentQuizAdmin)



class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
   inlines = [AnswerInline,]

admin.site.unregister(Question)
admin.site.register(Question,QuestionAdmin)



class QuestionInline(admin.TabularInline):
    model = Question

class QuizAdmin(admin.ModelAdmin):
   inlines = [QuestionInline,]

admin.site.unregister(Quiz)
admin.site.register(Quiz,QuizAdmin)
