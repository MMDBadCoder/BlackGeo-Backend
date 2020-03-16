from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, related_name="account")
    bio = models.TextField(max_length=120, default='nothing until now')
    activation_code = models.CharField(max_length=10, default='', blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
