from django.db import models
# import predefined User model

from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT
from django.db.models.fields.related import ForeignKey

# Create your models here.
class GoalStatus(models.Model):
    status_name = models.CharField(max_length=250)


    def __str__(self):
        return self.status_name 

class ScrumyGoals(models.Model):
    goal_name = models.CharField(max_length=250)
    goal_id = models.IntegerField()
    created_by = models.CharField(max_length=250)
    moved_by = models.CharField(max_length=250)
    owner = models.CharField(max_length=250)
    goal_status = models.ForeignKey(GoalStatus, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user')


    def __str__(self):
        return self.goal_name

class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length=250)
    created_by = models.CharField(max_length=250)
    moved_from = models.CharField(max_length=250)
    moved_to = models.CharField(max_length=250)
    time_of_action = models.DateTimeField()
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.PROTECT)

    def __str__(self):
        return self.created_by
