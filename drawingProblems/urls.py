from os import name

from drawingProblems import views
from django.conf.urls import url
from django.urls import path

app_name = 'drawingProblems'

urlpatterns = [
    path('s/<int:problem_id>/', views.problemPage_as_student, name='page-as-student'),
    path('t/<int:problem_id>/', views.problemPage_as_teacher, name='page-as-teacher'),
    path('set-details/<int:problem_id>/', views.set_details, name='set-details'),
    path('new/<int:set_id>/', views.new_problem, name='new-problem'),
    path('delete/<int:problem_id>/', views.delete_problem, name='delete'),
]
