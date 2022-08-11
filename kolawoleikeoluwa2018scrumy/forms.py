from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#create user form
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'first_name','last_name','email','username','password' ]


class CreateGoalForm(ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'user']

class MoveGoalForm(ModelForm):
    class Meta:
        model = ScrumyGoals

        fields = ['goal_status']



