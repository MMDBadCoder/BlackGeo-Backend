from django.db import models

# Create your models here.
from solutionManager.models import Solution


class DrawingSolution(Solution, models.Model):
    jsonObject = models.CharField(max_length=100000, blank=True, default=None)
    base64 = models.CharField(max_length=1000000, blank=True, default='')
    score = models.IntegerField(default=0)
    public = models.BooleanField(default=False)

    @staticmethod
    def get_solution(problem_id, username):
        try:
            solution = DrawingSolution.objects.get(account__user__username=username, problem__id=problem_id)
            return solution
        except:
            return None
