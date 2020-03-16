
from django.conf.urls import url
from accounting.forgot import views

urlpatterns = [
    url('send-email/', views.send_email, name='send-email'),
    url('check-authentication/', views.check_authentication, name='check-authentication'),
    url('new-password/', views.set_new_password, name='new-password'),
    url('', views.forgotPage, name='forgot'),
]
