from django.contrib import admin

# Register your models here.
from setManager.models import ProblemSet


@admin.register(ProblemSet)
class ProblemSetAdmin(admin.ModelAdmin):
    fields = ('title',)
    pass
