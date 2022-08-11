from django.contrib import admin

# Register your models here.

from .models import GoalStatus, ScrumyGoals, ScrumyHistory

myModels = [GoalStatus, ScrumyGoals, ScrumyHistory]  # iterable list
admin.site.register(myModels)
