from django.shortcuts import render


# Create your views here.
def problemPage_as_student(request):
    return render(request, 'drawing/teacher/teacher.html')


def problemPage_as_teacher(request):
    return render(request, 'drawing/teacher/teacher.html')
