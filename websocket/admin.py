from django.contrib import admin

# Register your models here.
from .models import Connection, ChatMessage

myModels = [Connection, ChatMessage]  # iterable list
admin.site.register(myModels)
