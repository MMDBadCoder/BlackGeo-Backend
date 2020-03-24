import json

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.shortcuts import render
from django.http import Http404, HttpResponseBadRequest, HttpResponse
from django.urls import reverse

from drawingProblems.models import DrawingProblem
from drawingSolutions.models import DrawingSolution


@login_required
def record_solution(request, problem_id):
    if not request.POST:
        return HttpResponseBadRequest
    jsonObject = request.POST.get('jsonObject')
    base64 = request.POST.get('base64')
    score = int(request.POST.get('score'))
    public = request.POST.get('public')

    last_solution = DrawingSolution.get_solution(problem_id, request.user.account)
    if (last_solution is not None):
        last_solution.jsonObject = jsonObject
        last_solution.base64 = base64
        last_solution.score = score
        last_solution.public = public
        last_solution.save()
    else:
        problem = DrawingProblem.objects.get(id=problem_id)
        DrawingSolution.objects.create(jsonObject=jsonObject, account=request.user.account, problem=problem,
                                       base64=base64, public=public, score=score)
    return HttpResponse(status=200)


@login_required
def solution_page(request, problem_id, username):
    problem = DrawingProblem.objects.get(id=problem_id)
    solution = DrawingSolution.get_solution(problem_id, username)
    if not solution:
        raise Http404
    if (not solution.public) and (solution.account != request.user.account):
        return HttpResponseBadRequest()
    return render(request, 'drawing/student/student.html', {'problem': problem, 'solution': solution})


def get_solutions(request, problem_id):
    solutions = DrawingSolution.objects.filter(problem__id=problem_id).order_by('-score')
    result = []
    for solution in solutions[0:10]:
        solution_address = reverse('drawingSolutions:solution-page',
                          kwargs={'problem_id': problem_id, 'username': solution.account.user.username})
        result.append({
            'score': solution.score,
            'public': solution.public,
            'name': str(solution.account.user),
            'href': solution_address
        })
    return HttpResponse(json.dumps(result), status=200)
