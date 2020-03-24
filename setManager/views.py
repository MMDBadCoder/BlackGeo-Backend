from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

from problemManager.models import Problem
from setManager.models import ProblemSet
from solutionManager.models import Solution


def problemSet_page(request, set_id):
    set = ProblemSet.objects.get(id=set_id)
    problems = set.problems.all()

    problem_and_solutions_by_id = dict()

    for problem in problems:
        problem_and_solutions_by_id[problem.id] = {'problem': problem, 'solution': None}

    total_score = 0
    if request.user.is_authenticated:
        solutions = Solution.objects.filter(problem__problem_set=set, account=request.user.account)
        for solution in solutions:
            problem_and_solution = problem_and_solutions_by_id[solution.problem.id]
            problem_and_solution['solution'] = solution
            total_score += solution.score

    problem_and_solutions = problem_and_solutions_by_id.values()

    return render(request, 'problemSet/problemSet-page.html',
                  {'set': set, 'problem_and_solutions': problem_and_solutions, 'total_score': total_score,
                   'top_accounts': set.get_top_accounts()})


@login_required
def new_set(request):
    set = ProblemSet.objects.create(author=request.user.account)
    return redirect('sets:page', set.id)


@login_required
def delete_set(request, set_id):
    set = ProblemSet.objects.filter(id=set_id, author=request.user.account)
    if not set.exists():
        return Http404()
    set.delete()
    return HttpResponse(status=200)


@login_required
def set_title(request, set_id):
    ProblemSet.objects.get(id=set_id, author=request.user.account).update(title=request.POST.get('title'))
    return HttpResponse(status=200)
