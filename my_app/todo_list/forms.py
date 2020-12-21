from django.forms import ModelForm,DateInput,Textarea
from .models import List, persons

class DateInput(DateInput):
    input_type = 'date'

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = '__all__'
        labels = {
            'desc': 'Description',
        }
        widgets = {
            'dueDate': DateInput(),
            'desc': Textarea(attrs={'cols': 80, 'rows': 2}),
           
        } 

class personsForm(ModelForm):
    class Meta:
        model = persons
        fields = ["name","email"] 
        