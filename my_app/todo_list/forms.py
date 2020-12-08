from django import forms
from .models import List, persons

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item","completed","priority","desc","dueDate","people"] 

class personsForm(forms.ModelForm):
    class Meta:
        model = persons
        fields = ["name","email"] 