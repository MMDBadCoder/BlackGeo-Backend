from django.contrib import admin

# Register your models here.
from problemManager.models import Problem


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    pass

