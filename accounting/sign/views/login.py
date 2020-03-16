from django.shortcuts import render


def loginGet(request):
    return render(request, 'accounting/sign.html', {'sign': 'login'})


def loginPost(request):
    return None
