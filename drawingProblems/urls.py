from django.conf.urls import url
from drawingProblems import views

urlpatterns = [
    url('', views.teacher, name='teacher-page'),
]
