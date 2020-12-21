from django.db import models
from django.forms.forms import Form 

# CREATE DATABASE MIGRATION: python manage.py makemigrations
# MIGRATE THE DATABASE: python manage.py migrate #
# use in terminal from 'todo_list.models import List' to query list table #

# create database table with attributes.

class persons(models.Model):
    name =  models.CharField(max_length=200)
    email = models.CharField(max_length=400,default='')   
    # so that name appears in select field
    def __str__(self): 
         return self.name
    
class List(models.Model):
    item =  models.CharField(max_length=200)
    desc = models.CharField(max_length=400,default='')
    PRIORITY_LEVELS = (
    ('1', 'High priority'),
    ('2', 'Medium priority'),
    ('3', 'Low priority')
    )
    priority = models.CharField(max_length=1, choices=PRIORITY_LEVELS,default='')
    completed = models.BooleanField(default=False)
    dueDate = models.DateField(null=True)
    people = models.ManyToManyField(persons)

    def __str__(self):
        return self.item + ' completed: ' + str(self.completed)


    