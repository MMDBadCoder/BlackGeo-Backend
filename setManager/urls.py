from django.conf.urls import url
from django.urls import path

from setManager import views

app_name = 'sets'

urlpatterns = [
    url('new/', views.new_set, name='new'),
    path('delete/<int:set_id>/', views.delete_set, name='delete'),
    path('<int:set_id>/', views.problemSet_page, name='page')
]
