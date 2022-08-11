from .models import ScrumyGoalsApi
from rest_framework import serializers

class ScrumyGoalsApiSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = ScrumyGoalsApi
       fields = ('goal_name', 'goal_id')


