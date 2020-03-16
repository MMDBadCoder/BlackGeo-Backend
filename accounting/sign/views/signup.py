import json

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render

from accounting.forms import UserSignUpForm
from accounting.models import Account


def signUpGet(request):
    return render(request, 'accounting/sign.html', {'sign': 'signup'})


def signUpPost(request):
    user_form = UserSignUpForm(request.POST)
    print(request.POST)

    if user_form.is_valid():

        email = user_form.cleaned_data.get('email')


        q = User.objects.filter(email=email, is_active=True)
        if q.exists():
            return HttpResponseBadRequest('There is an account with this email.')

        password = user_form.cleaned_data.get('password1')
        user = User.objects.create_user(username=email, password=password, email=email)
        user.is_active = True

        user.save()
        account = Account.objects.create(user=user)
        account.save()

        return HttpResponse(status=200)
    else:
        return HttpResponseBadRequest(str(user_form.errors))
