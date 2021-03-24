from django.db import models
from django.db.models.deletion import DO_NOTHING, CASCADE

class entity(models.Model):
    name = models.CharField(max_length=200,default=None, blank=True, null=True)
    id = models.AutoField(primary_key=True)

    def class_id(self):
        return f"{self.__class__.__name__}{self.id}"

    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True

class Task(entity):
    description = models.CharField(max_length=200)
    link = models.CharField(max_length=300,default=None, blank=True, null=True)


class Usertask(entity):
    upvote = models.BooleanField()
    usertasktask = models.ForeignKey(Task,on_delete=CASCADE)

    class Meta:
        ordering = ["-usertasktask"]