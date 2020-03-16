from http.client import HTTPResponse

from django.contrib.auth import authenticate, login
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, redirect


def loginPost(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(email)
    print(password)
    user = authenticate(request, username=email, password=password)
    if not user:
        return HttpResponseBadRequest('Incorrect email or password')
    login(request, user)
    return HttpResponse(status=200)

