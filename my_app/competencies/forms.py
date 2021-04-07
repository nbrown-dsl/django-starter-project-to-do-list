from django.forms import ModelForm,DateInput,Textarea,forms
from django import forms
from django.forms.widgets import CheckboxInput, CheckboxSelectMultiple
from .models import *

class DateInput(DateInput):
    input_type = 'date'

#created parent class so form classes can be searched as sub classes
class entityForm(ModelForm):
    abtract = True

class TaskForm(entityForm):
    class Meta:
        model = Task
        fields = ['name','description','link','system','requirement','role']
        

class UsertaskForm(entityForm):
    requirement = forms.ModelChoiceField(queryset= Requirement.objects.all(), empty_label="----",required=False)
    system = forms.ModelChoiceField(queryset= System.objects.all(), empty_label="----",required=False,initial='All systems')
    grade = forms.ModelChoiceField(queryset= grade.objects.all(), empty_label="----",required=False)
    description = forms.CharField(required=False)
    class Meta:
        model = Usertask
        fields = ['description','requirement','system','grade']
        # labels = {
        #     'fields': 'Form fields (ctrl to multiple select)'
        # }
        # widgets = { 'protocolFields': CheckboxSelectMultiple}

class gradeForm(entityForm):
    class Meta:
        model = grade
        fields = "__all__"
        
class requirementForm(entityForm):
    class Meta:
        model = Requirement
        fields = '__all__'

class systemForm(entityForm):
    class Meta:
        model = System
        fields = '__all__'





# class csvUploadForm(forms.ModelForm):
#   class Meta:
#     model = csvUpload
#     fields = ("csv_file",)

# class roleForm(entityForm):
#     class Meta:
#         model = Role
#         fields = '__all__'

# class profileForm(entityForm):
#     class Meta:
#         model = Profile
#         exclude = ['name']