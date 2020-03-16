
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from homeService import views as views

urlpatterns = [
    url('', views.homePage, name='home'),
]
