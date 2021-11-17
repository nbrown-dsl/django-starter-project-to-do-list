from django.db.models import fields
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import *
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import modelform_factory
from .syncDjango import *

import csv
import logging
import json

import os
import google_auth_oauthlib

from django.shortcuts import HttpResponseRedirect


#filterable list of users competencies according to role
def mycomps(request):
    user = request.user
    #check if user logged in. if not send to login page
    if not user.is_authenticated:
        return redirect ('login')
    #filter users tasks to those user has
    objects = Usertask.objects.filter(user=user)
    userskillsCount = objects.filter(userGrade__value__gte=1).count()
    #filters users tasks to those user has roles in and order by most votes first
    objects = objects.filter(usertasktask__role__in=user.groups.all()).order_by('-usertasktask__votes').distinct()
    
    if request.method == 'POST':
        form = UsertaskForm(request.POST or None)
        if form.is_valid():
            # requirement = form.cleaned_data['requirement']
            # if requirement: #ie requirement selected not 'all'
            #     objects = objects.filter(usertasktask__requirement__id=requirement.id)
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
       
    return render (request,'mycomps.html',{'objects':objects,'form':form, "numbers": range(4), 'count':userskillsCount})


#all competencies listed, regardless of user or role or votes
def allcomps(request):
    user = request.user
    #filter users tasks to those user has
    objects = Usertask.objects.filter(user=user)

    if request.method == 'POST':
        form = TaskFilterForm(request.POST or None)
        if form.is_valid():
            # requirement = form.cleaned_data['requirement']
            # if requirement: #ie requirement selected not 'all'
            #     objects = objects.filter(usertasktask__requirement__id=requirement.id)
            system = form.cleaned_data['system']
            if system: #ie system selected not 'all'
                objects = objects.filter(usertasktask__system__id=system.id)
            role = form.cleaned_data['role']
            if role: #ie system selected not 'all'
                objects = objects.filter(usertasktask__role__id=role.id)
            description = form.cleaned_data['description']
            objects = objects.filter(usertasktask__description__contains=description)
    else:
        form = TaskFilterForm(request.POST or None)

    return render(request,'allcomps.html',{'objects':objects,'form':form})

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

#from ajax javascript call upon click on star grade
def gradeChange(request):
        if request.method == 'GET':
            grade_value = request.GET.get('grade_value',3)
            usertask_id = request.GET.get('usertask_id',66)
            usertask = Usertask.objects.get(pk=usertask_id)
            oldnumber =  usertask.usertasktask.usersCompleted 
            #if previous user grade not same as grade checked then set as user grade
            # if (usertask.userGrade.value != int(grade_value)):
            if (int(grade_value)==0):
                newgrade = grade.objects.get(value=1) 
                usertask.userGrade = newgrade                
                newNumber = oldnumber + 1             
            #if previous grade same as checked, then unchecked and grade drops a level
            else:
                # lowervalue = int(grade_value)-1
                lowergrade = grade.objects.get(value=0)
                usertask.userGrade = lowergrade
                newNumber = oldnumber - 1

            usertask.usertasktask.usersCompleted = newNumber
            usertask.usertasktask.save(update_fields=['usersCompleted'])
            usertask.save(update_fields=['userGrade'])
            user = request.user
            userskills  = Usertask.objects.filter(user = user)
            userskillsCount = userskills.filter(userGrade__value__gte=1).count()

            datadict = { 'userskillsCount': userskillsCount, 'usersCompleted': newNumber }
            json_object = json.dumps(datadict, indent = 4)
            
            return HttpResponse(json_object) # Sending a success response

#from ajax javascript call upon click on upvote. changes vote and updates votes field accordingly
def vote(request):
        if request.method == 'GET':
            task_id = request.GET.get('task_id',66)
            task = Usertask.objects.get(pk=task_id)
            #toggle vote
            votes = task.usertasktask.votes
            if task.upvote:
                task.upvote = False  
                task.usertasktask.votes = votes - 1           
            else:
                task.upvote = True
                task.usertasktask.votes = votes + 1
            task.save(update_fields=['upvote'])
            task.usertasktask.save(update_fields=['votes'])
            
            return HttpResponse(str(task.usertasktask.votes)) # Sending a success response with updated number of votes
        
            
def profile(request):
    if request.method == 'POST':
        form = profileForm(request.POST or None,instance=request.user)
        if form.is_valid():
            form.save()
            print ("form valid")
            return redirect ('mycomps')

        else:
            print("form invalid")

    form = profileForm(request.POST or None, instance=request.user)
    
    return render(request,'profile.html',{'form':form})     
        
def skilledUsers(request):
   if request.method == 'GET': 
       task_id = request.GET.get('task_id',66)
       usertasks = Usertask.objects.filter(usertasktask = task_id).filter(userGrade__value__gte = 1)
       task = Task.objects.get(id=task_id)
       skillLink = task.link
       skillTitle = task.name
       skillDescription = task.description
       usersString = ""
       for user in usertasks:
           usersString += user.user.first_name + "<br>"
       datadict = { "usersString": usersString, "skillDescription": skillDescription, 'skillTitle': skillTitle, "skillLink": skillLink }
       json_object = json.dumps(datadict, indent = 3)

       return HttpResponse(json_object) # Sending who has skill to appear in modal

def sync(request):

    test_api_request()

    logging.getLogger("hello")

    return redirect('comps')


#from https://www.nishantwrp.com/posts/google-apis-oauth-in-django/

# The url where the google oauth should redirect
# after a successful login.
REDIRECT_URI = 'http://localhost:8000/google_oauth/callback/'

# Authorization scopes required
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Path of the "client_id.json" file
JSON_FILEPATH = os.path.join(os.getcwd(), 'google-credentials.json')

def RedirectOauthView(request):
    oauth_url = google_apis_oauth.get_authorization_url(
        JSON_FILEPATH, SCOPES, REDIRECT_URI)
    return HttpResponseRedirect(oauth_url)