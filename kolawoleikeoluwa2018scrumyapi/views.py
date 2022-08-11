from rest_framework import viewsets
from .serializers import ScrumyGoalsApiSerializer
from .models import ScrumyGoalsApi

# Create your views here.

class ScrumyGoalsViewSet(viewsets.ModelViewSet):
    queryset = ScrumyGoalsApi.objects.all().order_by('goal_name')
    serializer_class = ScrumyGoalsApiSerializer