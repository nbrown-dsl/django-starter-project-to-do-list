from django.forms import ModelForm,DateInput,Textarea
from django.forms.widgets import CheckboxInput, CheckboxSelectMultiple
from .models import *

class DateInput(DateInput):
    input_type = 'date'

class ListForm(ModelForm):
    # Provide an association between the ModelForm and a model

    class Meta():
        model = protocol
        p = protocol()
        fields = p.visibleFields()
        labels = {
            'surname': 'Surname',
        }
        widgets = {
            'arrivalDate': DateInput(),
            'leavingDate': DateInput(),
            #'surname': Textarea(attrs={'cols': 80, 'rows': 2}),        
        } 


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
        fields = ["TaskDescription","protocolType"] 


        