from .models import Answer, Question, Snippet, StudentAnswer, StudentQuiz, UserAssignment
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
    
class QuestionForm(forms.Form):     
    text = forms.CharField(max_length=100)
    def __init__(self, *args, question, **kwargs):
        self.q_text = question.text
        super().__init__(*args, **kwargs)                                  #

        
class QuizForm(forms.ModelForm):
    class Meta:
        model = StudentAnswer
        fields = '__all__'
    

class BaseQuestionFormSet(forms.BaseFormSet):
    def get_form_kwargs(self, index):
        kwargs = self.form_kwargs
        print('aaaaa')
        print(self.form_kwargs.get('questions')) 
        print(self.data)
        print(self.extra)
        print()
        print('fuuuk')
        # note that instead of passing a dictionary which includes a copy
        # of the formset's form_kwargs, we actually return a dictionary
        # that holds a single key-value pair
        return {'question': {'text':'lol'}}                                                                                                 #returns question object from forms index in a list
