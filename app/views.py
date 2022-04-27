import os
from django.views import generic
from django.shortcuts import render
from app.constants import SOLUTIONS_FOLDER, TEMPLATES_FOLDER
from app.helpers import download_file
from uoop.settings import BASE_DIR
from .forms import QuizForm, SnippetForm, AssignmentForm
from .models import Assignment, Course, Question, Quiz, Snippet, StudentAnswer, Test, TestCase
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
    testCases = TestCase.objects.filter(assignment=id)
    context = {}
    passedTests = []
    failedTests = []
    context['assignment'] = Assignment.objects.get(id=id)
    context['visibleTests'] = TestCase.objects.filter(
        assignment=id).filter(isVisible=True)
    context['tags'] = context['assignment'].tags.all()
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            for testCase in testCases:
                ans = subprocess.check_output(
                    ['java', '-jar', os.path.join(mediaPath, request.FILES['jar'].name)], input=testCase.input.encode(), timeout=testCase.time)
                if(ans == testCase.output.encode()):
                    passedTests.append(testCase)
                else:
                    failedTests.append(testCase)
            context['form'] = form
            context['passedTests'] = passedTests
            context['failedTests'] = failedTests
            return render(request, 'assignment.html', context)
    else:
        form = AssignmentForm()
    context['form'] = form
    context['passedTests'] = passedTests
    context['failedTests'] = failedTests
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
    quizs = Quiz.objects.get(id=id)
    questions = list(Question.objects.filter(quiz_id = id))
    #answers = list(Answer.objects.filter(quiz__id = id).)
    studentAnswers= StudentAnswer.objects.filter(answer__question__quiz=id)
    if request.method == 'POST':
        form = QuizForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home/')
        else:
            return redirect('home/') 
            #return render(request, 'quiz.html', {'quizs':quizs, 'questions':questions, 'studentAnswers':studentAnswers})
    else:
        form = QuizForm()     
    return render(request, 'quiz.html', {'quizs':quizs, 'questions':questions, 'studentAnswers':studentAnswers})

# Function used to download jar solution file for specific assignment
def download_solution(request, id):
    return download_file(id, SOLUTIONS_FOLDER)

# Function used to download jar template file for specific assignment
def download_template(request, id):
    return download_file(id, TEMPLATES_FOLDER)

