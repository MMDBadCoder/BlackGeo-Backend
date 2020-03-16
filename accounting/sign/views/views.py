from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect


def signUpRequest(request):
    print('signUpRequest')
    import accounting.sign.views.signup as signup
    if request.POST:
        return signup.signUpPost(request)
    return signup.signUpGet(request)


def loginPage(request):
    import accounting.sign.views.login as login
    if request.POST:
        return login.loginPost(request)
    return render(request, 'accounting/sign.html', {'sign': 'login'})


def forgotPage(request):
    return render(request, 'accounting/forgot.html')


@login_required
def logoutRequest(request):
    logout(request)
    return redirect('login')
