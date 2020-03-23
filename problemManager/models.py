from django.db import models
from setManager.models import ProblemSet


class Problem(models.Model):
    name = models.CharField(max_length=50, blank=True, default='No named yet')
    description = models.CharField(max_length=1000, blank=True, default='No description yet')
    base64 = models.CharField(max_length=10000, blank=True, default='')
    problem_set = models.ForeignKey(to=ProblemSet, on_delete=models.CASCADE, related_name='problems', default=None,
                                    null=True)

    @staticmethod
    def can_edit(problem, account):
        return problem.problem_set.author is account
