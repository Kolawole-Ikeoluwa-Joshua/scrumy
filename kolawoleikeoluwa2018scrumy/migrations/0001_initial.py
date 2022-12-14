# Generated by Django 3.2.8 on 2021-10-22 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GoalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyGoals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_name', models.CharField(max_length=250)),
                ('goal_id', models.IntegerField()),
                ('created_by', models.CharField(max_length=250)),
                ('moved_by', models.CharField(max_length=250)),
                ('owner', models.CharField(max_length=250)),
                ('goal_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kolawoleikeoluwa2018scrumy.goalstatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moved_by', models.CharField(max_length=250)),
                ('created_by', models.CharField(max_length=250)),
                ('moved_from', models.CharField(max_length=250)),
                ('moved_to', models.CharField(max_length=250)),
                ('time_of_action', models.DateTimeField()),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kolawoleikeoluwa2018scrumy.scrumygoals')),
            ],
        ),
    ]
