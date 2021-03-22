from django.forms import ModelForm,DateInput,Textarea,forms
from django import forms
from django.forms.widgets import CheckboxInput, CheckboxSelectMultiple
from .models import *

class DateInput(DateInput):
    input_type = 'date'

class TaskForm(ModelForm):   

    class Meta():
        model = Task

        fields = "__all__"
        

class UsertaskForm(ModelForm):
    class Meta:
        model = Usertask
        fields =  "__all__"



        