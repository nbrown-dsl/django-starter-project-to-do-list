from django.forms import ModelForm,DateInput,Textarea,forms
from django import forms
from django.forms.widgets import CheckboxInput, CheckboxSelectMultiple
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class DateInput(DateInput):
    input_type = 'date'

#created parent class so form classes can be searched as sub classes
class entityForm(ModelForm):
    abtract = True

class TaskFilterForm(ModelForm):
    # requirement = forms.ModelChoiceField(queryset= Requirement.objects.all(), empty_label="----",required=False)
    system = forms.ModelChoiceField(queryset= System.objects.all().order_by('name'), empty_label="----",required=False,initial='All systems')
    role = forms.ModelChoiceField(queryset= Group.objects.all(), empty_label="----",required=False)
    description = forms.CharField(required=False)
    class Meta:
        model = Usertask
        fields = ['description','system','role'] 

class TaskForm(entityForm):
    class Meta:
        model = Task
        fields = ['name','description','link','system','role']
        help_texts = {'link':'URL to resource that explains how to learn competency. It could be video, webpage, doc, etc etc',
        'name': 'A pithy summary of competency',
        'description': 'A fuller description of competency',
        'role': 'Select which role this competency applies to. Shift select to select multiple roles'}

       
class UsertaskForm(entityForm):
    # requirement = forms.ModelChoiceField(queryset= Requirement.objects.all(), empty_label="----",required=False)
    system = forms.ModelChoiceField(queryset= System.objects.all().order_by('name'), empty_label="System...",required=False,initial='All systems',widget=forms.Select(attrs={'class': 'form-control'}))
    grade = forms.ModelChoiceField(queryset= grade.objects.filter(value__lte=1),required=False,widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    description = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Search...'}))
    class Meta:
        model = Usertask
        fields = ['description','system','grade']


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

class profileForm(ModelForm):
    class Meta:
        model = User
        fields = ['groups','first_name','last_name','email']
        labels = {'groups':'Roles'}
        help_texts = {'groups':'Shift select to select multiple roles'}



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