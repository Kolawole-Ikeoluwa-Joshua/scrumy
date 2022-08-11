from django.urls import path,include
from . import views

urlpatterns = [
    path('success/', views.success, name="success"),
    path('', views.index, name="index"),
    path('movegoal/<int:goal_id>', views.move_goal, name='movegoal'),
    path('addgoal/', views.add_goal, name='addgoal'),
    path('home/', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls'))
]
