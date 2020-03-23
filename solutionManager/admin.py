from django.contrib import admin
from solutionManager.models import Solution


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    pass

