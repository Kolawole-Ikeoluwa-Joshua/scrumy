from django.db import models

# Create your models here.
class ScrumyGoalsApi(models.Model):
    goal_name = models.CharField(max_length=250)
    goal_id = models.IntegerField(default=1)
    created_by = models.CharField(max_length=250)
    
    def __str__(self):
        return self.goal_name