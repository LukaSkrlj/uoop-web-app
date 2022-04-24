from django.http import Http404
from django.views import generic
from django.shortcuts import render
from .forms import SnippetForm, AssignmentForm
from .models import Assignment, Course, Snippet, Test, TestCase
from django.shortcuts import render, redirect
from django.core.files import File
import subprocess
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse

mediaPath = 'C:\\Users\\Skerlj\\Desktop\\izprojekt\\uoop\\media\\'
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
                    ['java', '-jar', mediaPath + request.FILES['jar'].name], input=testCase.input.encode(), timeout=testCase.time)
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


def home(request):
    courses = Course.objects.all()
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
    return redirect('home/')



def osustavu(request):
    return render(request, 'osustavu.html')

def automatiziranaprovjera(request):
    return render(request, 'automatiziranaprovjera.html')

# Function used to download jar file
def download(request, id):
    # find the current assignment in database
    assignment = Assignment.objects.get(id=id)

    # get fileName from current assignment
    fileName = os.path.basename(assignment.assignmentTemplate.name)

    #fileName should not be None
    if fileName == None:
        return Http404()

    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Define the full file path
    filepath = BASE_DIR + '/media/assignment_templates/' + fileName

    # Open the file for reading content
    path = open(filepath, 'rb')

    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)

    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)

    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % fileName

    # Return the response value
    return response
