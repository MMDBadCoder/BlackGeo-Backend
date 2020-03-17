from django.db import models


# Create your models here.


class ProblemSet(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')


class DrawingProblem(models.Model):
    name = models.CharField(max_length=50, blank=True, default='No named yet')
    description = models.CharField(max_length=1000, blank=True, default='No description yet')
    goals_elements = models.CharField(max_length=1000, blank=True, default='')
    base64 = models.CharField(max_length=10000, blank=True, default='')
    set = models.ForeignKey(ProblemSet, null=True, default=None, on_delete=models.CASCADE)
