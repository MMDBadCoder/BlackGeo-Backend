from django.contrib import admin
from drawingSolutions.models import DrawingSolution


@admin.register(DrawingSolution)
class DrawingSolutionAdmin(admin.ModelAdmin):
    pass

