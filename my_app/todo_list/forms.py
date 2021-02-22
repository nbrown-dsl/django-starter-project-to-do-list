from django.forms import ModelForm,DateInput,Textarea,forms
from django import forms
from django.forms.widgets import CheckboxInput, CheckboxSelectMultiple
from .models import *

class DateInput(DateInput):
    input_type = 'date'

class ListForm(ModelForm):   

    class Meta():
        model = protocol

        fields = "__all__"
        # exclude = ["type"]
        widgets = { 'arrivalDate': DateInput,
                    'leavingDate': DateInput}
        

class personsForm(ModelForm):
    class Meta:
        model = persons
        fields = ["name","email"] 

class protocolTypeForm(ModelForm):
    class Meta:
        model = protocoltype
        fields = '__all__'
        labels = {
            'fields': 'Form fields (ctrl to multiple select)'
        }
        widgets = { 'protocolFields': CheckboxSelectMultiple}

class taskForm(ModelForm):
    
    class Meta:
        model = task
        fields = ["TaskDescription","protocolType","person"] 
        labels = { 'person': 'Responsibility'}

class filterForm(ModelForm):
    
    protocols = forms.ModelChoiceField(queryset= protocol.objects.all(), initial="No filter")
    

    class Meta:
        
        model = task
        fields = ["person","protocols","protocolType"]
        labels = { 'person': 'Responsibility',
                    'protocols': 'Protocol',
                    'protocolType': 'Type of protocol'}

    
    
        



        