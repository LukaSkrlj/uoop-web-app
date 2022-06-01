import os
from django.forms import formset_factory
from django.views import generic
from django.shortcuts import render
from app.constants import SOLUTIONS_FOLDER, TEMPLATES_FOLDER
from app.helpers import download_file
from uoop.settings import BASE_DIR
from .forms import BaseQuestionFormSet, QuestionForm, QuizForm, SnippetForm, AssignmentForm
from .models import Assignment, Course, NewUser, Question, Quiz, Snippet, StudentAnswer, StudentQuiz, Test, TestCase, UserAssignment, UserTestCase
from django.shortcuts import render, redirect
from django.core.files import File
import subprocess
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

mediaPath = os.path.join(BASE_DIR, 'media')
filePath = 'C:\\Users\\Skerlj\\Desktop\\izprojekt'


class CoursesView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.all()  # u template object_list courses ust


class TestsView(generic.DetailView):
    template_name = 'course.html'


def simple(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            f = open(filePath + '\\test.java', 'w')
            testfile = File(f)
            testfile.write(request.POST.get('text'))
            testfile.close
            f.close

            process = subprocess.Popen("C:\\Users\\Skerlj\\Desktop\\izprojekt\\test.bat", shell=True, universal_newlines=True,
                                       stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf8')
            out, err = process.communicate()
            print(out, err)
            # print(settings.BASE_DIR)

            return redirect('/simple')
    else:
        form = SnippetForm()
    return render(request, "form.html", {
        "form": form,
        "snippets": Snippet.objects.all()
    })


def main(request):
    return render(request, 'main.html')


def course(request, id):
    course = Course.objects.get(id=id)
    tests = Test.objects.filter(course=id)
    quizs = Quiz.objects.filter(course=id)
    print(course, tests, quizs)
    return render(request, 'course.html', {'course': course, 'tests': tests, 'quizs': quizs})


def test(request, id):
    test = Test.objects.get(id=id)
    assignments = Assignment.objects.filter(test=id)
    print(assignments, test)
    return render(request, 'test.html', {'test': test, 'assignments': assignments})


def assignment(request, id):
    # fetch all test cases related to current assignment
    testCases = TestCase.objects.filter(assignment=id)

    #initialize context
    context = {}
    
    # find the user assignment if it exists
    userAssignment = UserAssignment.objects.filter(
        assignment=id, newuser=request.user.id).first()

    # fetch all users test cases
    context['userTestCases'] = UserTestCase.objects.filter(userassignment=userAssignment)

    # get current assignment
    context['assignment'] = Assignment.objects.get(id=id)

    # get all tags related to this assignment
    context['tags'] = context['assignment'].tags.all()

    # initialize test cases array
    context['allTests'] = []

    # filter only thets which are visible
    context['visibleTests'] = TestCase.objects.filter(isVisible=True)

    # if user submited the form run his submited file
    if request.method == 'POST':
        # initialize form with request data
        form = AssignmentForm(request.POST, request.FILES)

        if form.is_valid():
            # save the form if it is valid
            form.save()

            # if userAssignment does not exist create a new instance 
            if(userAssignment is None):
                userAssignment = UserAssignment(assignment=context['assignment'], newuser=request.user)
                userAssignment.save()

            # if run the code for each test case
            for testCase in testCases:
                ans = subprocess.check_output(
                    ['java', '-jar', os.path.join(mediaPath, request.FILES['jar'].name)], input=testCase.input.encode(), timeout=testCase.timeLimit)
                userTestCase = UserTestCase.objects.filter(userassignment=userAssignment, testcase=testCase).first()
               
                # if the test case does not exist create a new one
                if(userTestCase is None):
                    userTestCase = UserTestCase(userassignment=userAssignment, testcase=testCase)

                # If answered correctly test case field isCorrect should be assigned true, by default it is false
                if(ans == testCase.output.encode()):
                    userTestCase.is_correct=True
                else: 
                    userTestCase.is_correct=False
                userTestCase.save()
                # sppend all test cases
                context['allTests'].append(userTestCase)
            context['form'] = form
            context['userAssignment'] = userAssignment
            
            # render the page with context object
            return render(request, 'assignment.html', context)
    else:
        # if user didn't sumbmit the form instantiate a new one and pass it to context
        form = AssignmentForm()
    context['form'] = form

    # render the page with context object
    return render(request, 'assignment.html', context)

def getStartDateYear(course):
    return str(course['startDate']).split("-")[0]

def home(request):
    tmp = Course.objects.values()
    courses = {}
    
    for course in tmp:
        if courses.get(str(course['startDate']).split("-")[0]) == None:
            courses[getStartDateYear(course)] = [course]
        else:
            courses[getStartDateYear(course)].append(course)

    return render(request, 'home.html', {'courses': courses})


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


def login_user(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/')

def osustavu(request):
    return render(request, 'osustavu.html')

def automatiziranaprovjera(request):
    return render(request, 'automatiziranaprovjera.html')

def quiz(request, id):
    context = {}
    correctAnswers = []
    incorrectAnswers = []

    quizs = Quiz.objects.get(id=id)
    studentAnswers = StudentAnswer.objects.filter(answer__question__quiz=id)
    questions = Question.objects.filter(quiz_id = id)
    studentQuiz= StudentQuiz()
    studentQuiz.percentage = 0
    mainform = QuizForm(instance = studentQuiz)
    #QuizFormset = inlineformset_factory(StudentQuiz, StudentAnswer, fields = '__all__', min_num = 0, max_num = questions.count(), extra = 0)
    ###QuizFormset = modelformset_factory(StudentAnswer, exclude = ('studentQuiz','question'), extra = 0,  max_num = questions.count(), min_num = 0)

    qs = list(Question.objects.filter(quiz_id = id))
    QuizFormset = formset_factory(QuestionForm, formset=BaseQuestionFormSet, extra=len(qs))#extra = 0,  max_num = questions.count(), min_num = questions.count())
    formset = QuizFormset(form_kwargs={'questions': qs})

    context['quizs'] = quizs
    context['studentAnswers'] = studentAnswers
    context['questions'] = questions
    context['form'] = mainform
    context['formset'] = formset

    print(context['quizs'])
    print(context['questions'])
    print(context['studentAnswers'])

    
    if request.method == 'POST':
        mainform = QuizForm(request.POST)
        formset = QuizFormset(request.POST)
        if mainform.is_valid():
            for form in formset:
                instance = form.save(commit = False)
                instance.studentQuiz = studentQuiz
                instance.save()
                print("SAVE")
            context['form'] = mainform
            context['formset'] = formset
            context['correctAnswers'] = correctAnswers
            context['incorrectAnswers'] = incorrectAnswers
            print("POSTvalid!")
            instance = mainform.save(commit = False)
            instance.quiz = Quiz.objects.get(id=id)
            instance.student = NewUser.objects.get(email=request.user.get_username())
            instance.save()
            return render(request, 'courses.html', context)
        else:
            print(mainform.errors)
            print("POST.FORMINvalid!")
            mainform = QuizForm()
            context['form'] = mainform
            print(mainform.errors)
            print("POST.FORMINvalid!")
            return render(request, 'quiz.html', context)
    print("GET!")
    return render(request, 'quiz.html', context)

# Function used to download jar solution file for specific assignment
def download_solution(request, id):
    return download_file(id, SOLUTIONS_FOLDER)

# Function used to download jar template file for specific assignment
def download_template(request, id):
    return download_file(id, TEMPLATES_FOLDER)

