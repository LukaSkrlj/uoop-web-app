from django.urls import path
from app import views

app_name = 'uoop'
urlpatterns = [
    path("", views.main, name="main"),
    path("home/", views.home, name="home"),
    path("test/<int:id>/", views.test, name="test"),
    path("course/<int:id>/", views.course, name="courses"),
    path("assignment/<int:id>/", views.assignment, name="assignment"),
    path("login_user", views.login_user, name="login_user"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("simple", views.simple, name="simple"),
    path("upload", views.upload, name="upload"),
    path('download/<int:id>', views.download, name="download"),
    # path("course/<int:id>", views.course, name="course"),
    # path("ispit/<name>", views.test, name="test"),
    # path("zadatak/<int:id>", views.assignment, name="assignment"),
]
