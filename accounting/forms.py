from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)
