from django import forms
from .models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item","completed"] 

class searchForm(forms.Form):
    searchTerm = forms.CharField(label='search', max_length=100)