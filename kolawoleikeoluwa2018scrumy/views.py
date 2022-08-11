from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from .models import ScrumyGoals, GoalStatus
from django.contrib.auth.models import User, Group
from .forms import MoveGoalForm, SignupForm, CreateGoalForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
import random






def success(request):
    context = {'success_message':"Your account has been created successfully"}
    return render(request, 'kolawoleikeoluwa2018scrumy/success.html', context)



def index(request): 
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            my_group = Group.objects.get(name = 'Developer')
            used = form.save()
            my_group.user_set.add(used) 
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            
            return render(request, 'kolawoleikeoluwa2018scrumy/success.html', {'success_message': 'Your account has been created successfully'})
    else:
        form = SignupForm()
    
    context = {'form': form}
    
    return render(request, 'kolawoleikeoluwa2018scrumy/index.html', context)


@login_required
def move_goal(request, goal_id):
    target_goal = ScrumyGoals.objects.get(goal_id=goal_id)
    old_goal_status = target_goal.goal_status.status_name
    current_user = request.user
    form = MoveGoalForm()
    if request.method == "POST":
        form = MoveGoalForm(request.POST, instance=target_goal)
        if form.is_valid():
            # Developer
            if current_user.groups.filter(name='Developer').exists():
                if current_user.username == target_goal.owner and old_goal_status != 'Done Goal':
                    form.save()
                    return render(request, 'kolawoleikeoluwa2018scrumy/success.html', {'success_message': 'Update Successful'})

                else:
                    goal = ScrumyGoals.objects.get(goal_id=goal_id)
                    goal.save()
                    form = MoveGoalForm()
                    context = {
                        'form':form,
                        'goal_name':goal,
                        'error_message':'You can only move goals you created. You also do not have permission to set a goal as Done Goal'
                    }
                    return render(request, 'kolawoleikeoluwa2018scrumy/movegoal.html', context)

            # Quality Assurance
            elif current_user.groups.filter(name='Quality Assurance').exists():
                if current_user.username == target_goal.owner:
                    form.save()
                    return render(request, 'kolawoleikeoluwa2018scrumy/success.html', {'success_message': 'Update Successful'})

                elif old_goal_status == 'Verify Goal' or old_goal_status == 'Done Goal':
                    form.save()
                    return render(request, 'kolawoleikeoluwa2018scrumy/success.html', {'success_message': 'Update Successful'})

                else:
                    goal = ScrumyGoals.objects.get(goal_id=goal_id)
                    goal.save()
                    form = MoveGoalForm()
                    context = {
                        'form': form,
                        'goal_name': goal,
                        'error_message': 'You can only move goals from Verify To Done if they were not created by you'
                    }
                    return render(request, 'kolawoleikeoluwa2018scrumy/movegoal.html', context)



            # Owner
            elif current_user.groups.filter(name='Owner').exists():
                if current_user.username == target_goal.owner: 
                    form.save()
                    return render(request, 'kolawoleikeoluwa2018scrumy/success.html',  {'success_message': 'Your goal has been updated successfully'})
                else:
                    goal = ScrumyGoals.objects.get(goal_id=goal_id)
                    goal.save()
                    form = MoveGoalForm()
                    context = {
                        'form': form,
                        'goal_name': goal,
                        'error_message': 'You do not have the permission to move this goal because you belong to the Owner group and did not create this goal'
                    }
                    return render(request, 'kolawoleikeoluwa2018scrumy/movegoal.html', context)

            # Admin
            elif current_user.groups.filter(name='Admin').exists():
                form.save()
                return render(request, 'kolawoleikeoluwa2018scrumy/success.html',  {'success_message': 'Your goal has been updated successfully'})
            else:
                goal = ScrumyGoals.objects.get(goal_id=goal_id)
                goal.save()
                form = MoveGoalForm()
                context = {
                    'form': form,
                    'goal_name': goal,
                    'error_message': 'You do not belong to any group'
                }
                return render(request, 'kolawoleikeoluwa2018scrumy/movegoal.html', context)


    else:
        goal = ScrumyGoals.objects.get(goal_id=goal_id)
        goal.save()
        context = {'form': form, 'goal_name':goal, 'user': request.user}
        return render(request, 'kolawoleikeoluwa2018scrumy/movegoal.html', context)







def add_goal(request):

    # ssecond version of add_goal view

    weekly_goals = GoalStatus.objects.get(status_name='Weekly Goal')

    form = CreateGoalForm()

    if request.method == 'POST':
        form = CreateGoalForm(request.POST)
        if form.is_valid():

            f = form.save(commit=False)

            random_id = random.randint(1000, 9999)
            user = form.cleaned_data['user']
            myuser = User.objects.get(username=user)

            f.goal_id = random_id
            f.goal_status = weekly_goals
            f.created_by = myuser
            f.moved_by = myuser
            f.owner = myuser

            f.save()

    else:
        form = CreateGoalForm()


    context = {'form': form}

    return render(request, 'kolawoleikeoluwa2018scrumy/addgoal.html', context) 


def home(request):
    users = User.objects.all()
    weekly_goals = GoalStatus.objects.get(status_name='Weekly Goal')
    related_weekly_goal = weekly_goals.scrumygoals_set.all()
    daily_goals = GoalStatus.objects.get(status_name='Daily Goal')
    related_daily_goal = daily_goals.scrumygoals_set.all()
    verify_goals = GoalStatus.objects.get(status_name='Verify Goal')
    related_verify_goal = verify_goals.scrumygoals_set.all()
    done_goals = GoalStatus.objects.get(status_name='Done Goal')
    related_done_goal = done_goals.scrumygoals_set.all()

    context = {
        'users':users,
        'related_weekly_goal':related_weekly_goal,
        'related_daily_goal':related_daily_goal,
        'related_verify_goal':related_verify_goal,
        'related_done_goal':related_done_goal,

    }
    return render(request, 'kolawoleikeoluwa2018scrumy/home.html', context)
