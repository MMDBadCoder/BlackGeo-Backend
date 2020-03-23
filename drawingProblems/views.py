from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from drawingProblems.models import DrawingProblem
from django.http import Http404, HttpResponse, HttpResponseBadRequest

from drawingSolutions.models import DrawingSolution
from problemManager.models import Problem
from setManager.models import ProblemSet


def problemPage_as_student(request, problem_id):
    problem = DrawingProblem.objects.get(id=problem_id)
    return render(request, 'drawing/student/student.html', {'problem': problem})


@login_required
def problemPage_as_teacher(request, problem_id):
    problem = DrawingProblem.objects.get(id=problem_id)
    if Problem.can_edit(problem, request.user.account):
        return render(request, 'drawing/teacher/teacher.html', {'problem': problem})
    else:
        return HttpResponseBadRequest()


@login_required
def new_problem(request, set_id):
    set = ProblemSet.objects.get(id=set_id)
    if set.author is request.user.account:
        problem = DrawingProblem.objects.create(problem_set=set)
        return redirect('drawing:page-as-teacher', problem.id)
    else:
        return HttpResponseBadRequest()


@login_required
def delete_problem(request, problem_id):
    problem = DrawingProblem.objects.get(id=problem_id)
    if Problem.can_edit(problem, request.user.account):
        DrawingProblem.objects.filter(id=problem_id).delete()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseBadRequest()


def set_details(request, problem_id):
    problem = DrawingProblem.objects.get(id=problem_id)
    if not Problem.can_edit(problem, request.user.account):
        return HttpResponseBadRequest()
    goals = request.POST.get('goals')
    costs = request.POST.get('costs')
    name = request.POST.get('name')
    description = request.POST.get('description')
    base64 = request.POST.get('base64')
    problem.update(costs=costs, goals_elements=goals, name=name,
                   description=description, base64=base64)
    return HttpResponse(status=200)
