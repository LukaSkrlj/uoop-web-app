from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [
    path("home/", views.home, name="home"),
    path("quiz/<int:id>/", views.quiz, name="quiz"),
    path("test/<int:id>/", views.test, name="test"),
    path("course/<int:id>/", views.course, name="courses"),
    path("assignment/<int:id>/", views.assignment, name="assignment"),
    path("login_user/", views.login_user, name="login_user"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("simple/", views.simple, name="simple"),
    path("upload/", views.upload, name="upload"),
    path("automatiziranaprovjera/", views.automatiziranaprovjera,
         name="automatiziranaprovjera"),
    path("osustavu/", views.osustavu, name="osustavu"),
    path('download_template/<int:id>',
         views.download_template, name="download_template"),
    path('download_solution/<int:id>',
         views.download_solution, name="download_solution"),
    path('input/<int:id>', views.input, name="input"),
    path('output/<int:id>', views.output, name="output"),
]
