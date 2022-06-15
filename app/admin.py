from django.contrib import admin

# Register your models here.

from app.models import Answer, Course, Question, Quiz, StudentAnswer, StudentQuiz, Test, Assignment, TestCase, Tag, UserAssignment, UserTestCase

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
admin.site.register(UserTestCase)
admin.site.register(StudentQuiz)

#giving StudentQuiz inlines which contain StudentAnswers- for a simpler admin interface 
class StudentAnswerInline(admin.TabularInline):        
    model = StudentAnswer
    extra = 0

class StudentQuizAdmin(admin.ModelAdmin):
   inlines = [StudentAnswerInline,]

admin.site.unregister(StudentQuiz)
admin.site.register(StudentQuiz,StudentQuizAdmin)


#giving Question inlines which contain Answers- for a simpler admin interface 
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
   inlines = [AnswerInline,]
   extra = 0

admin.site.unregister(Question)
admin.site.register(Question,QuestionAdmin)


#giving Quiz inlines which contain Questions- for a simpler admin interface 
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2

class QuizAdmin(admin.ModelAdmin):
   inlines = [QuestionInline,]

admin.site.unregister(Quiz)
admin.site.register(Quiz,QuizAdmin)
