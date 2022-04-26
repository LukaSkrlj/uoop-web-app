from dataclasses import fields
from .models import Snippet, StudentAssignment , StudentAnswer
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
        model = StudentAssignment
        fields = ('jar',)
    

class QuizForm(forms.ModelForm):
    class Meta:
        model = StudentAnswer
        fields = '__all__'