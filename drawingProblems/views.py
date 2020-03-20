from django.shortcuts import render, redirect
from drawingProblems.models import DrawingProblem
from django.http import Http404, HttpResponse, HttpResponseBadRequest

from setManager.models import ProblemSet


def problemPage_as_student(request, problem_id):
    try:
        problem = DrawingProblem.objects.get(id=problem_id)
        return render(request, 'drawing/student/student.html', {'problem': problem})
    except:
        raise Http404



def problemPage_as_teacher(request, problem_id):
    try:
        problem = DrawingProblem.objects.get(id=problem_id)
        return render(request, 'drawing/teacher/teacher.html', {'problem': problem})
    except Exception as e:
        print(e)
        raise Http404


def new_problem(request, set_id):
    set = ProblemSet.objects.get(id=set_id)
    problem = DrawingProblem.objects.create(problem_set=set)
    return redirect('drawing:page-as-teacher', problem.id)


def delete_problem(request, problem_id):
    DrawingProblem.objects.filter(id=problem_id).delete()
    return redirect(request.META.get('HTTP_REFERER'))


def set_details(request, problem_id):
    goals = request.POST.get('goals')
    costs = request.POST.get('costs')
    name = request.POST.get('name')
    description = request.POST.get('description')
    base64 = request.POST.get('base64')
    DrawingProblem.objects.filter(id=problem_id).update(costs=costs, goals_elements=goals, name=name,
                                                        description=description, base64=base64)
    return HttpResponse(status=200)
