from django.shortcuts import render
from django.views.generic import ListView
from .models import Usertask




# Create your views here.
class taskList(ListView):

    model = Usertask


    


