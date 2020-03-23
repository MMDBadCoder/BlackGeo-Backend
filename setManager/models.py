from django.contrib.auth.models import User
from django.db import models


class ProblemSet(models.Model):
    title = models.CharField(max_length=100, blank=True, default='Untitled')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, null=True)

    def __str__(self):
        return self.title