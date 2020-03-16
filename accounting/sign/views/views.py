from django.http import HttpResponseBadRequest
from django.shortcuts import render

def signUpRequest(request):
    import accounting.views.signup as signup
    if request.GET:
        return signup.signUpGet(request)
    if request.POST:
        return signup.signUpPost(request)
    return HttpResponseBadRequest('not supported type of request(only get and post)')



def loginPage(request):
    import accounting.views.login as login
    if request.GET:
        return login.loginGet(request)
    if request.POST:
        return login.loginPost(request)
    return HttpResponseBadRequest('not supported type of request(only get and post)')


def forgotPage(request):
    return render(request, 'accounting/forgot.html')

