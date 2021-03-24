from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import DO_NOTHING, CASCADE, SET_NULL

User = get_user_model()

class entity(models.Model):
    name = models.CharField(max_length=200,default=None, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    #method to return id that is unique across all models
    def class_id(self):
        return f"{self.__class__.__name__}{self.id}"

    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True

class System(entity):
    link = models.CharField(max_length=300,default=None, blank=True, null=True)


class Task(entity):
    description = models.CharField(max_length=200)
    link = models.CharField(max_length=300,default=None, blank=True, null=True)
    system = models.ForeignKey(System,on_delete=SET_NULL, null=True)


class grade(entity):
   description = models.CharField(max_length=200)
   value = models.IntegerField() 
   
class Usertask(entity):
    upvote = models.BooleanField()
    usertasktask = models.ForeignKey(Task,on_delete=CASCADE)
    userGrade = models.ForeignKey(grade,on_delete=SET_NULL, null=True, default = 4)
    user = models.ForeignKey(User,on_delete=CASCADE)

    class Meta:
        ordering = ["-usertasktask"]

