import random
import string
import threading

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


def send_email(request):
    print(request.POST)
    email = request.POST.get('email')
    user = User.objects.filter(username=email)
    if not user.exists():
        return HttpResponseBadRequest('Incorrect email')
    user = user.get()
    code = get_random_code(6)
    print('code', code)
    user.account.activation_code = code
    user.account.save()
    current_site = get_current_site(request)
    data = {
        'domain': current_site.domain,
        'code': code,
    }
    html_content = render_to_string('accounting/activation.html', data)
    subject, from_email, to = 'Password recovery', 'joorabnakhi@gmail.com', email
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")

    def send():
        msg.send()

    threading.Thread(target=send, args=()).start()

    print('send')

    return HttpResponse(status=200)


def check_authentication(request):
    print(request.POST)
    code = request.POST.get('code')
    email = request.POST.get('email')
    user = User.objects.filter(email=email, account__activation_code=code)
    if (not user.exists()) or (code == ''):
        return HttpResponseBadRequest('Incorrect code')
    return HttpResponse(status=200)


def set_new_password(request):
    print(request.POST)
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if password1 != password2:
        return HttpResponseBadRequest('The two password fields didn’t match.')
    code = request.POST.get('code')
    email = request.POST.get('email')
    user = User.objects.filter(email=email, account__activation_code=code)
    if (not user.exists()) or (code == ''):
        return HttpResponseBadRequest('Invalid code or email')
    user = user.get()

    user.set_password('new_password')

    request.POST._mutable = True
    request.POST.update({'old_password': 'new_password'})
    request.POST._mutable = False

    form = PasswordChangeForm(user, request.POST)

    if not form.is_valid():
        print(form.cleaned_data)
        return HttpResponseBadRequest(str(form.errors))

    user.set_password(password1)
    form.save()

    return HttpResponse(status=200)


def forgotPage(request):
    return render(request, 'accounting/forgot.html')


def get_random_code(length):
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(length))
