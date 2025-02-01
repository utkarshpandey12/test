from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Tasks, Users


# URL Configuration
urlpatterns = [
    path("tasks", Tasks.as_view(), name="task_api"),
    path("users", Users.as_view(), name="users_api"),
]
