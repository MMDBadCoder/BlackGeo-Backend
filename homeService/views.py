from django.shortcuts import render

# Create your views here.
from setManager.models import ProblemSet


def homePage(request):
    sets = ProblemSet.objects.all()
    return render(request, 'home/home.html', {'sets': sets})
