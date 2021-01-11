from django.forms import ModelForm,DateInput,Textarea
from .models import List, persons

class DateInput(DateInput):
    input_type = 'date'

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = '__all__'
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
        