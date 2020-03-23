from django.urls import path
from . import views

app_name = 'drawingSolutions'

urlpatterns = [
    path('record-solution/<int:problem_id>', views.record_solution, name='record-solution'),
    path('<int:problem_id>/<str:username>/', views.solution_page, name='solution-page')
]
