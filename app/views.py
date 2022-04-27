from cmath import log
from pickle import TRUE
from django.http import Http404
from django.views import generic
from django.shortcuts import render
from app.constants import SOLUTIONS_FOLDER, TEMPLATES_FOLDER

from app.helpers import download_file
from .forms import SnippetForm, AssignmentForm
from .models import Assignment, Course, Snippet, Test, TestCase, UserAssignment, UserTestCase
from django.shortcuts import render, redirect
from django.core.files import File
import subprocess
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# mediaPath = 'C:\\Users\\Skerlj\\Desktop\\izprojekt\\uoop\\media\\'
# mediaPath = 'C:\\Users\\Borna\\Documents\\DJANGO\\uoop-web-app\\media\\' #svatko svoje treba stavit ili preko env file-a
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
    print(tests)
    return render(request, 'course.html', {'course': course, 'tests': tests})


def test(request, id):
    test = Test.objects.get(id=id)
    assignments = Assignment.objects.filter(test=id)
    print(assignments, test)
    return render(request, 'test.html', {'test': test, 'assignments': assignments})


def assignment(request, id):
    testCases = TestCase.objects.filter(assignment=id)
    context = {}
    context['userAssignment'] = UserAssignment.objects.filter(
        assignment=id, newuser=request.user.id)
    context['userTestCases'] = UserTestCase.objects.filter(userassignment=context['userAssignment'])
    context['assignment'] = Assignment.objects.get(id=id)
    context['visibleTests'] = TestCase.objects.filter(
        assignment=id).filter(isVisible=True)
    context['tags'] = context['assignment'].tags.all()
    allTests = []
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if(context['userAssignment'] is None):
                userAssignment = UserAssignment(assignment=context['assignment'], newuser=request.user)
                userAssignment.save()
            for testCase in testCases:
                ans = subprocess.check_output(
                    ['java', '-jar', mediaPath + request.FILES['jar'].name], input=testCase.input.encode(), timeout=testCase.time_limit)
                userTestCase = UserTestCase.objects.filter(userassignment=context['userAssignment'], testCase=testCase)
                if(userTestCase.exists() != None):
                    userTestCase = UserTestCase(userAssignment=userAssignment, testCase=testCase)
                # If answered correctly test case field isCorrect should be assigned true, by default it is false
                if(ans == testCase.output.encode()):
                    userTestCase.is_correct=True
                    userTestCase.testcase.is_visible=True
                userTestCase.save()
                allTests.append(userTestCase)
            context['form'] = form
            context['allTests'] = allTests
            return render(request, 'assignment.html', context)
    else:
        form = AssignmentForm()
    context['form'] = form
    context['allTests'] = TestCase
   
        
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
            return redirect('home/')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/')

# Function used to download jar solution file for specific assignment
def download_solution(request, id):
    return download_file(id, SOLUTIONS_FOLDER)

# Function used to download jar template file for specific assignment
def download_template(request, id):
    return download_file(id, TEMPLATES_FOLDER)



