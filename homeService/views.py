from django.shortcuts import render

# Create your views here.
from setManager.models import ProblemSet


def homePage(request):
    sets = ProblemSet.objects.all()
    # ProblemSet.objects.all().delete()
    return render(request, 'home/home.html', {'sets': sets})


def test(request):
    return render(request, 'problemSet/test.html')
