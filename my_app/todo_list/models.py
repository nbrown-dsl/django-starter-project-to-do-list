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
    forename =  models.CharField(max_length=50,default='')
    surname = models.CharField(max_length=50,default='')
    YEAR_LEVELS = (
    ('1', 'yr 1'),
    ('2', 'yr 2'),
    ('3', 'yr 3')
    )
    yearLevel = models.CharField(max_length=1, choices=YEAR_LEVELS,default='')
    completed = models.BooleanField(default=False)
    arrivalDate = models.DateField(null=True)
    leavingDate = models.DateField(null=True)
    people = models.ManyToManyField(persons)

    def __str__(self):
        return self.item + ' completed: ' + str(self.completed)


    