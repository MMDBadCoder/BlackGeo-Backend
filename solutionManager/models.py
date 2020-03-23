from django.db import models

# Create your models here.
from accounting.models import Account
from problemManager.models import Problem


class Solution(models.Model):
    problem = models.ForeignKey(Problem, null=True, default=None, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, null=True, default=None, on_delete=models.CASCADE)
