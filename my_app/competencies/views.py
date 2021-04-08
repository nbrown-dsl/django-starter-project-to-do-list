from django.db.models import fields
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import *
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import modelform_factory

import csv
import logging




# # Create your views here.
# class taskList(ListView):
#     template_name = 'comps.html'
#     model = Usertask
    # def get(self, request):
    #     # <view logic>
    #     return render(request,'competencies/comps.html')

def mycomps(request):
    #user task instances filtered by current user
    # f = usertaskFilter(request.GET, queryset=Usertask.objects.filter(user=request.user))
    # return render (request,'mycomps.html',{'filter':f,'form':form})
    objects = Usertask.objects.filter(user=request.user)
    if request.method == 'POST':
        form = UsertaskForm(request.POST or None)
        if form.is_valid():
            requirement = form.cleaned_data['requirement']
            if requirement: #ie requirement selected not 'all'
                objects = objects.filter(usertasktask__requirement__id=requirement.id)
            system = form.cleaned_data['system']
            if system: #ie system selected not 'all'
                objects = objects.filter(usertasktask__system__id=system.id)
            grade = form.cleaned_data['grade']
            if grade: #ie system selected not 'all'
                objects = objects.filter(userGrade__id=grade.id)
            description = form.cleaned_data['description']
            objects = objects.filter(usertasktask__description__contains=description)
    else:
        form = UsertaskForm(request.POST or None)
        
    return render (request,'mycomps.html',{'objects':objects,'form':form, "numbers": range(4)})



def comps(request):
    objectList = []
    for table in entity.__subclasses__():
        objectList.append({'name':table.__name__,'objects':table.objects.all()})


    return render (request,'comps.html',{'objectDic':objectList})

#for saving form submissions    
def saveForm(request,object):
    foundModel = False
    #if object is name of model, ie new instance 
    for formClass in entityForm.__subclasses__():
                if formClass.Meta.model.__name__ == object:
                    form = formClass(request.POST or None)
                    foundModel = True
    #if object is id rather than model name then it is class_id and need to save pre-existing instance
    if not foundModel:
                        
        for table in entity.__subclasses__():
                for instance in table.objects.all():
                    if instance.class_id() == object:
                        for formClass in entityForm.__subclasses__():
                            if formClass.Meta.model.__name__ == table.__name__:
                                form = formClass(request.POST or None, instance = instance)
      

    if form.is_valid():
            form.save() 


    return redirect ('comps')
   

#for rendering forms
def renderForm(request,object):
    #for rendering unbound form for adding new instance
    foundModel = False
    for formClass in entityForm.__subclasses__():
            if formClass.Meta.model.__name__ == object:
                form = formClass()
                foundModel = True#for rendering bound form from exisitng instance

    if not foundModel:
    
        for table in entity.__subclasses__():
                    for instance in table.objects.all():
                        if instance.class_id() == object:
                            editInstance = table.objects.get(pk=instance.id)
                            formObject = modelform_factory(table,fields=("__all__"))
                            form = formObject(instance=editInstance)

    return render (request,'renderForm.html',{'formObject':form, 'object': object})


def deleteInstance(request,objectID):
    for table in entity.__subclasses__():
                    for instance in table.objects.all():
                        if instance.class_id() == objectID:
                            instance.delete()
    return redirect ('comps')
    
#forget it - too difficult - hard ot get upload data in correct format to be accepted, esp role field
def importCSV(request,object):
    if request.method =="POST":
        csvuploadfile = request.FILES["csv_file"]
        try:
            form = csvUploadForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                csv_file = form.cleaned_data['csv_file']
            if not csv_file.name.endswith('.csv'):
                return redirect('uploadForm')

            file_data = csv_file.read().decode('utf-8')
            lines = file_data.split('\n')
        # with open(csvuploadfile, newline='') as csvfile:
            headers = lines[0].split(',')
            
            for row in range(1,len(lines)-1):
                fields = lines[row].split(',')
                data_dict = {}
                for cell in range(len(fields)):
                    if headers[cell] == 'role':
                        data_dict[headers[cell]] = fields[cell].split(',')
                    else:
                        data_dict[headers[cell]] = fields[cell]
                print(data_dict)
            try:
                form = TaskForm(data_dict)
                if form.is_valid():
                    form.save()
                else:
                    logging.getLogger('error_logger').error(form.errors.as_json())
            except Exception as e:
                logging.getLogger('error_logger').error(form.errors.as_json())
                pass
        except Exception as e:
            logging.getLogger('error_logger').error('Unable to upload file. ' + repr(e))
            # messages.error(request, 'Unable to upload file. ' + repr(e))
                       
        return redirect ('comps')
        
    else:
        form = csvUploadForm()
        return render (request,'uploadForm.html',{'object': object, 'form':form})

#response to download button, returns csv file of model instances
def exportCSV(request,entityName):
    #create array of field names to be be csv headers
    for table in entity.__subclasses__():
        print(table.__name__)
        print(entityName)
        if table.__name__ == str(entityName):
            fields = table._meta.fields
            fieldnames = []
            for field in fields:
                fieldnames.append(field.name)

            tasks = table.objects.all()
            
        # Create the HttpResponse object with the appropriate CSV header.
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="tasks.csv"'

            writer = csv.DictWriter(response,fieldnames=fieldnames)
            writer.writeheader()
            for task in tasks:
                row={}
                for fieldname in fieldnames:
                    row.update({fieldname:str(getattr(task,fieldname))})
                writer.writerow(row)

            return response
    
    return redirect('comps')

#from ajax javascript call
def gradeChange(request):
        print("hello")
        if request.method == 'GET':
            grade_value = request.GET.get('grade_value',0)
            usertask_id = request.GET.get('usertask_id',66)
            grade1 = grade.objects.get(value=int(grade_value)) 
            usertask = Usertask.objects.get(pk=usertask_id)
            #if previous user grade not same as grade checked then set as user grade
            if (usertask.userGrade.value != grade_value):
                usertask.userGrade = grade1
                usertask.save(update_fields=['userGrade'])
            # if item.completed:
            #     item.completed = False
            # else:
            #     item.completed = True
            # item.save()
            print("grade changed from "+ str(usertask.userGrade.value) + " to " + str(grade_value))
            return HttpResponse("Success!") # Sending an success response
        
            
        
        