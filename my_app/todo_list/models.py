from django.db import models
# CREATE DATABASE MIGRATION: python manage.py makemigrations
# MIGRATE THE DATABASE: python manage.py migrate #
# use in terminal from 'todo_list.models import List' to query list table #

# create database table with attributes.

class List(models.Model):
    item =  models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' completed: ' + str(self.completed)