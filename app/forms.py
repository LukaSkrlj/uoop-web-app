from .models import Snippet, StudentAnswer, UserAssignment
from django import forms
from django_ace import AceWidget


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        widgets = {
            "text": AceWidget(mode='java', theme='dracula'),
        }
        exclude = ()


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = UserAssignment
        fields = ('jar',)
    

class QuizForm(forms.ModelForm):
    class Meta:
        model = StudentAnswer
        fields = '__all__'