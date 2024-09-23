# tasks/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('task/new/', views.task_form, name='task_form'),
    # other paths
]
