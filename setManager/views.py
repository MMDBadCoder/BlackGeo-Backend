from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from setManager.models import ProblemSet


def problemSet_page(request, set_id):
    set = ProblemSet.objects.get(id=set_id)
    return render(request, 'problemSet/problemSet-page.html', {'set': set})


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
