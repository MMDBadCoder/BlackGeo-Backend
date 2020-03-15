from django.shortcuts import render


def signUpPage(request):
    return render(request, 'accounting/sign.html', {'sign': 'signup'})


def loginPage(request):
    return render(request, 'accounting/sign.html', {'sign': 'login'})


def forgotPage(request):
    return render(request, 'accounting/forgot.html')

