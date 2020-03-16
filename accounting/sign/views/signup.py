from django.shortcuts import render


def signUpGet(request):
    return render(request, 'accounting/sign.html', {'sign': 'signup'})


def signUpPost(request):
    pass