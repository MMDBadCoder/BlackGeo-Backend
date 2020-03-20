from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from setManager.models import ProblemSet


def problemSet_page(request, set_id):
    set = ProblemSet.objects.get(id=set_id)
    return render(request, 'problemSet/problemSet-page.html', {'set': set})


def new_set(request):
    set = ProblemSet.objects.create()
    return redirect('sets:page', set.id)


def delete_set(request, set_id):
    set = ProblemSet.objects.filter(id=set_id)
    if not set.exists():
        return Http404()
    set.delete()
    return HttpResponse(status=200)


def set_title(request, set_id):
    ProblemSet.objects.get(id=set_id).update(title=request.POST.get('title'))
    return HttpResponse(status=200)
