
from django.conf.urls import url

from accounting.sign.views import views

urlpatterns = [
    url('up/', views.signUpRequest, name='signup'),
    url('in/', views.loginPage, name='login'),
    url('out/', views.logoutRequest, name='logout'),
    url('/', views.signUpRequest, name='signup'),
]
