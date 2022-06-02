from .models import Answer, Snippet, StudentAnswer, StudentQuiz, UserAssignment
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
    
class QuestionForm(forms.ModelForm):                                
    def __init__(self, *args, question, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)                                                                         #calling constructor
        self.fields['answer'] = forms.ModelChoiceField(queryset = Answer.objects.filter(question_id = question.id), 
                                                        label = question.text, widget=forms.RadioSelect)                            #dynamically generationg radio form                                                                                  #dynamically adding question text 
        self.question = question    	                                                                                            #dynamically adding question to a form
        #super().__init__(*args, **kwargs)                                                                                          https://forum.djangoproject.com/t/pass-different-parameters-to-each-form-in-formset/4040/2
    class Meta:
        model = StudentAnswer                                                                                               
        exclude = ('studentQuiz', 'question')                                                                                       #removing fields for these foreign key models
        answer = forms.ModelChoiceField(widget=forms.RadioSelect, queryset=Answer.objects.none())                                   #

        
class QuizForm(forms.ModelForm):
    class Meta:
        model = StudentQuiz
        exclude = ('quiz', 'student','percentage')
    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
    

class BaseQuestionFormSet(forms.BaseFormSet):                                                                                       #used to pass different data parameters from list to each form
    def get_form_kwargs(self, index):
        kwargs = super().get_form_kwargs(index)
        q = kwargs['questions'][index]                  
        return {'question': q}                                                                                                      #returns question object from forms index in a list
