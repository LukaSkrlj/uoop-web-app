import os
from django.forms import formset_factory
from django.views import generic
from django.shortcuts import render
from app.constants import SOLUTIONS_FOLDER, TEMPLATES_FOLDER
from app.helpers import download_file
from uoop.settings import BASE_DIR
from .forms import SnippetForm, AssignmentForm
from .models import Answer, Assignment, Course, NewUser, Question, Quiz, Snippet, StudentAnswer, StudentQuiz, Test, TestCase, UserAssignment, UserTestCase
from django.shortcuts import render, redirect
from django.core.files import File
from subprocess import PIPE, check_output, Popen
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

            process = Popen("C:\\Users\\Skerlj\\Desktop\\izprojekt\\test.bat", shell=True, universal_newlines=True,
                            stdin=PIPE, stdout=PIPE, stderr=PIPE, encoding='utf8')
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

    # initialize context
    context = {}

    # find the user assignment if it exists
    userAssignment = UserAssignment.objects.filter(
        assignment=id, newuser=request.user.id).first()

    # fetch all users test cases
    context['userTestCases'] = UserTestCase.objects.filter(
        userassignment=userAssignment)

    # get current assignment
    context['assignment'] = Assignment.objects.get(id=id)

    # get all tags related to this assignment
    context['tags'] = context['assignment'].tags.all()

    # initialize test cases array
    context['allTests'] = []

    # filter only tests which are visible and belong to that assignment
    context['visibleTests'] = TestCase.objects.filter(
        assignment=id, isVisible=True)

    # if user submited the form run his submited file
    if request.method == 'POST':
        # if userAssignment does not exist create a new instance
        if(userAssignment is None):
            userAssignment = UserAssignment(
                assignment=context['assignment'], newuser=request.user)
            userAssignment.save()

        form = AssignmentForm(request.POST, request.FILES,
                              instance=userAssignment)

        if form.is_valid():
            # save the form if it is valid
            form.save()

            try:
                junitTestsOut, junitTestErr = Popen('java -cp ' + os.path.join(mediaPath, request.FILES['jar'].name) + ';' + os.path.join(
                    BASE_DIR, 'junit.jar junit.textui.TestRunner ' + context['assignment'].test_class), stdin=PIPE, stderr=PIPE, stdout=PIPE).communicate()
                context['junit'] = junitTestsOut.decode(
                    "utf-8") + junitTestErr.decode("utf-8")
            except:
                print('JUNIT ERROR')

            # if run the code for each test case
            for testCase in testCases:
                ans = check_output(
                    ['java', '-jar', os.path.join(mediaPath, request.FILES['jar'].name)], input=testCase.input.encode(), timeout=testCase.timeLimit)

                userTestCase = UserTestCase.objects.filter(
                    userassignment=userAssignment, testcase=testCase).first()

                # if the test case does not exist create a new one
                if(userTestCase is None):
                    userTestCase = UserTestCase(
                        userassignment=userAssignment, testcase=testCase)

                # If answered correctly test case field isCorrect should be assigned true, by default it is false
                if(ans == testCase.output.encode()):
                    userTestCase.is_correct = True
                else:
                    userTestCase.is_correct = False

                userTestCase.user_output = ans.decode()  # decode because it's byte encoding

                userTestCase.save()
                # append all test cases
                context['allTests'].append(userTestCase)
            context['userAssignment'] = userAssignment
            context['form'] = form

            # render the page with context object
            return render(request, 'assignment.html', context)
    else:
        # if user didn't sumbmit the form instantiate a new one and pass it to context
        # TODO: nakon sta se fixa UserAssignment vidjet ako je user vec izvrtio testcaseove za ovaj zadatak i onda samo to displayat
        form = AssignmentForm(instance=userAssignment)
        context['form'] = form

    # render the page with context object
    return render(request, 'assignment.html', context)


def getStartDateYear(course):
    return str(course['startDate']).split("-")[0]


def input(request, id):
    input = TestCase.objects.get(id=id).input
    context = {}
    context["txt"] = input
    return render(request, "input_output.html", context)


def output(request, id):
    output = TestCase.objects.get(id=id).output
    context = {}
    context["txt"] = output
    return render(request, "input_output.html", context)


def home(request):
    tmp = Course.objects.values()
    courses = {}

    for course in tmp:
        if courses.get(getStartDateYear(course)) == None:
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
            return redirect('app:home')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('app:home')


def osustavu(request):
    return render(request, 'osustavu.html')


def automatiziranaprovjera(request):
    return render(request, 'automatiziranaprovjera.html')


def quiz(request, id):
    # fetching data from database
    quizs = Quiz.objects.get(id=id)
    questions = list(Question.objects.filter(quiz_id=id))
    studentAnswers = list(
        StudentAnswer.objects.filter(answer__question__quiz=id))
    # disables student from submitting more than one quiz
    quizvisible = 1
    if(StudentQuiz.objects.filter(quiz=quizs).filter(student=(NewUser.objects.get(email=request.user.get_username()))).exists()):
        quizvisible = 0
        studentQuizs = StudentQuiz.objects.filter(quiz=quizs).get(
            student=(NewUser.objects.get(email=request.user.get_username())))
    else:
        studentQuizs = None
    if request.method == 'POST':  # quiz submitted
        if(StudentQuiz.objects.filter(quiz=quizs).filter(student=(NewUser.objects.get(email=request.user.get_username()))).exists()):
            print("exists")
        else:
            # creating studentQuiz object with available data
            studQuiz = StudentQuiz.objects.create(quiz=Quiz.objects.get(
                id=id), student=NewUser.objects.get(email=request.user.get_username()))
            scoredPoints = 0
            for question in questions:  # iterating through question objects in quiz
                # fetching selected radio button value
                response = request.POST.get(str(question.text))

                # creating studentQuiz object with answer object
                if(response != None):
                    answer = Answer.objects.filter(
                        text=response).get(question_id=question.id)
                    studAnswer = StudentAnswer.objects.create(
                        studentQuiz=studQuiz, question=question, answer=answer)
                    if(answer.true):  # incrementing scored points
                        scoredPoints += question.points
                        StudentAnswer.objects.filter(
                            id=studAnswer.id).update(points=question.points)

                 # creating studentQuiz object without answer object
                else:
                    studAnswer = StudentAnswer.objects.create(
                        studentQuiz=studQuiz, question=question)

            # saving percentage and points data to studentQuiz
            if(quizs.points > 0):  # avoiding division by zero error
                scoredPercentage = (scoredPoints/quizs.points)*100
                StudentQuiz.objects.filter(id=studQuiz.id).update(
                    percentage=scoredPercentage)

            StudentQuiz.objects.filter(
                id=studQuiz.id).update(points=scoredPoints)

            return redirect('app:home')
        return redirect('app:home')
    # accessing quiz.html first time
    else:
        return render(request, 'quiz.html', {'quizs': quizs, 'questions': questions, 'studentAnswers': studentAnswers, 'quizvisible': quizvisible, 'studentQuizs': studentQuizs})

# Function used to download jar solution file for specific assignment


def download_solution(request, id):
    return download_file(id, SOLUTIONS_FOLDER)

# Function used to download jar template file for specific assignment


def download_template(request, id):
    return download_file(id, TEMPLATES_FOLDER)
