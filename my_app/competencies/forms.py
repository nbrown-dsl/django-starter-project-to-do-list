from django.forms import ModelForm,DateInput,Textarea,forms
from django import forms
from django.forms.widgets import CheckboxInput, CheckboxSelectMultiple
from .models import *

class DateInput(DateInput):
    input_type = 'date'

class entityForm(ModelForm):
    abtract = True

class TaskForm(entityForm):
    class Meta:
        model = Task
        fields = "__all__"

class UsertaskForm(entityForm):
    class Meta:
        model = Usertask
        fields = "__all__"

        