from django.contrib import admin

from drawingProblems.models import DrawingProblem


@admin.register(DrawingProblem)
class DrawingProblemAdmin(admin.ModelAdmin):
    pass

