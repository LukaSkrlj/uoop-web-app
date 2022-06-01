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
        #super(QuestionForm, self).__init__(*args, **kwargs)
        #super().__init__(*args, **kwargs)
        #self.fields['answer'] = forms.ModelChoiceField(queryset = Answer.objects.filter(question_id = question.id), label = question.text, widget=forms.RadioSelect)
        #self.fields['answer'].queryset = Answer.objects.filter(question_id = question.id)
        #self.fields['answer'].label = question.text
        #super().__init__(*args, **kwargs)
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['answer'] = forms.ModelChoiceField(queryset = Answer.objects.filter(question_id = question.id), label = question.text, widget=forms.RadioSelect)
        #self.fields['answer'].queryset = Answer.objects.filter(question_id = question.id)
        #self.fields['answer'].widget=forms.RadioSelect
        self.fields['answer'].label = question.text
        self.question = question
        #super(QuestionForm, self).__init__(*args, **kwargs)
    class Meta:
        model = StudentAnswer
        exclude = ('studentQuiz', 'question')
        answer = forms.ModelChoiceField(widget=forms.RadioSelect, queryset=Answer.objects.none())
        
        #######answer = forms.ChoiceField(choices= Answer.objects.filter(question_id = question.id), label = question.text, widget=forms.RadioSelect)
       # author = forms.ModelMultipleChoiceField(queryset=Answer.objects.all())
        
        #super().__init__(*args, **kwargs)
    
     # 'question')
        #answer = forms.ModelMultipleChoiceField(queryset=None)
        ###answer = forms.ModelChoiceField(choices = Answer.objects.all(), label = "pitanje", widget=forms.RadioSelect)#choices = Answer.objects.filter(question_id = idq), label = "pitanje", widget=forms.RadioSelect)
        #if my_bool:
         #   self.fields['question'] = forms.CharField(max_length=256)
        #question = 
        
        #fields = '__all__'

        
class QuizForm(forms.ModelForm):
    class Meta:
        model = StudentQuiz
        exclude = ('quiz', 'student','percentage')
    
        #if my_bool:
         #   self.fields['question'] = forms.CharField(max_length=256)
    def __init__(self, *args, **kwargs):
       # self._idq = kwargs.pop('idq', None)
        super(QuizForm, self).__init__(*args, **kwargs)
    

class BaseQuestionFormSet(forms.BaseFormSet):
    def get_form_kwargs(self, index):
        kwargs = super().get_form_kwargs(index)
        q = kwargs['questions'][index]
        # note that instead of passing a dictionary which includes a copy
        # of the formset's `form_kwargs`, we actually return a dictionary
        # that holds a single key-value pair
        return {'question': q}

#QuizFormset = inlineformset_factory(StudentQuiz, StudentAnswer, fields = '__all__')#, QuestionForm)