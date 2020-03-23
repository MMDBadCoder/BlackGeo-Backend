from atexit import register

from django.contrib import admin

# Register your models here.
from accounting.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass