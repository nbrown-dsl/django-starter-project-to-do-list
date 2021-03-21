from django.db import models
from django.db.models.deletion import DO_NOTHING

class entity(models.Model):
    name = models.CharField(max_length=200,default="TBC")
    
    class Meta:
        abstract = True

class Task(entity):
    description = models.CharField(max_length=200)

class Usertask(entity):
    upvote = models.BooleanField()
    usertasktask = models.ForeignKey(Task,on_delete=DO_NOTHING)

    class Meta:
        ordering = ["-usertasktask"]