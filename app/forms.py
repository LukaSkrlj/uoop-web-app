from dataclasses import fields
from .models import Snippet, UserAssignment
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
