from django.db import models

# Create your models here.
class ContactModel(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

class TaskBoard(models.Model):
    taskName = models.CharField(max_length=100)
    endDate = models.DateField()
    
    

    