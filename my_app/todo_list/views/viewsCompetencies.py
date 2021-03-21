from django.shortcuts import render, redirect
from ..models import *
from ..forms import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect, HttpResponse
# module to read string from entity list as class name
import sys
from django.core.mail import send_mail
from django.conf import settings
# from django.views.generic import ListView

# # Create your views here.
# class taskList(ListView):
    
#     model = persons
    # def get(self, request):
    #     # <view logic>
    #     return render(request,'todo_list/objectlist.html')