from django.db import models
from django.db.models.deletion import DO_NOTHING




class Task(models.Model):
    description = models.CharField(max_length=200)

class Usertask(models.Model):
    upvote = models.BooleanField()
    task = models.ForeignKey(Task,on_delete=DO_NOTHING)