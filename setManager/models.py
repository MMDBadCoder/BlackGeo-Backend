from django.db import models


class ProblemSet(models.Model):
    title = models.CharField(max_length=100, blank=True, default='Untitled')

    def __str__(self):
        return self.title