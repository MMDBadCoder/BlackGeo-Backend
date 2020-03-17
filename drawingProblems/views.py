from django.shortcuts import render


def teacher(request):
    return render(request, 'drawing/teacher/teacher.html')