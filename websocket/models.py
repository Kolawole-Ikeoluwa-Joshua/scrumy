from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Connection(models.Model):
    connection_id = models.CharField(max_length=255)


    def __str__(self):
        return self.connection_id

class ChatMessage(models.Model):
    username = models.CharField(max_length=50)
    message = models.CharField(max_length=400)
    timestamp = models.CharField(max_length=100)

    def __str__(self):
        return self.username

        