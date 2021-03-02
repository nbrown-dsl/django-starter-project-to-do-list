from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
# module to read string from entity list as class name
import sys
from django.core.mail import send_mail
from django.conf import settings



protocolName = "All protocols"
personName = "All people"
protocolTypeName = "All types"


def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

# Create your views here.
def home(request):
    #if from filter form
    all_items = taskdata.objects.order_by('protocol').all()
    #for populating dropdown menus
    protocols = protocol.objects.all()
    people = persons.objects.all()
    protocoltypeObjects = protocoltype.objects.all()

    #form filter form request, cumalatively builds up filter queryset
    if request.method == 'POST':
        global form
        form = filterForm(request.POST or None)
        if form.is_valid():
            global protocolName
            protocolName = form.cleaned_data['protocols']
            if str(protocolName) != "All protocols":
                all_items = all_items.filter(protocol__forename__contains=protocolName)
            global personName
            personName = form.cleaned_data['person']
            if str(personName) != "All people":
                all_items = all_items.filter(task__person__name__contains=personName)
            global protocolTypeName
            protocolTypeName = form.cleaned_data['protocolType']
            if str(protocolTypeName) != "All types":
                all_items = all_items.filter(protocol__type__protocolTypeName__contains=protocolTypeName)
            
            messages.success(request,('Filtered'))
    #redirect from uncross/cross or initial rendering or clear
    else:
        #flag for clearing form or not 
        clearForm = True
        if str(protocolName) != "All protocols":
                all_items = all_items.filter(protocol__forename__contains=protocolName)
                clearForm = False
        if str(personName) != "All people":
                all_items = all_items.filter(task__person__name__contains=personName)
                clearForm = False
        if str(protocolTypeName) != "All types":
                all_items = all_items.filter(protocol__type__protocolTypeName__contains=protocolTypeName) 
                clearForm = False
        #sets form to no filters
        if clearForm:
            form = filterForm({'person':4,'protocols':24, 'protocolType':6})  
    
    all_items = all_items.order_by('protocol')
    
    return render(request,'home.html',{'all_items' : all_items,'people' : people,'protocoltype':protocoltypeObjects,'protocols':protocols, 'filterForm': form})

def protocolAdd(request,type):
    typeObject = protocoltype.objects.get(pk=type) 

    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            newprotocol = form.instance
            tasks = task.objects.filter(protocolType = typeObject)
            for protocoltask in tasks:
                newTask = taskdata(task=protocoltask,protocol=newprotocol)
                newTask.save()
            messages.success(request,('Protocol created'))
        else:
            messages.success(request,(form.errors))
        return redirect('home')
    else: 
        newProtocol = protocol()
        newProtocol.type = typeObject 
        form = ListForm(instance=newProtocol)
        removeFields(form,newProtocol)
        # visible_fields = newProtocol.visibleFields()
        # visible_fields.append('type')
        # invisible_fields = []
        # #generates array of field names not to show on form
        # for field in form.fields:
        #     if field not in visible_fields:
        #         invisible_fields.append(field)
        # #removes fields not to show from field dictionary        
        # for field in invisible_fields :
        #     if field in form.fields:
        #         form.fields.pop(field)
    #set filter attribute from list of fields in type object
        protocoltypeName = typeObject.protocolTypeName
        return render(request,'protocolAdd.html',{'form' : form, 'protocoltype' : protocoltypeName})

# orders items alphabetically
# def order(request):    
#     # order items (minus sign for descending order) use eg [:5] at end of line to limit items returned
#     people = persons.objects.all
#     all_items = List.objects.order_by('item')
    
#     return render(request,'home.html',{'all_items' : all_items,'people' : people})

#filter list of protocols
def filter(request,query,model):
    filtered_items = taskdata.objects.all()

    if query == "all" or len(query)<1:
        
        messages.success(request,('All items')) 

    else:# filters across models using name of manaytomanyfield then attribute in related model, separated by __
        if model=="person":
            filtered_items = taskdata.objects.filter(task__person__id=query)
        if model=="protocol":
            filtered_items = taskdata.objects.filter(protocol__id=query)
        
        if len(filtered_items) == 0:
            messages.success(request,('No filtered items')) 

    protocols = protocol.objects.all
    people = persons.objects.all
    protocoltypeObjects = protocoltype.objects.all
    
    return render(request,'home.html',{'all_items' : filtered_items,'people' : people,'protocoltype':protocoltypeObjects,'protocols':protocols})  

def clear(request):
    global protocolName
    protocolName = "All protocols"
    global personName
    personName = "All people"
    global protocolTypeName
    protocolTypeName = "All types"
    return redirect ('home')

def about(request):
    my_name ="Nick"
    return render(request,'about.html',{'name' : my_name})

def delete(request, list_id):
    item = protocol.objects.get(pk=list_id)
    item.delete()
    messages.success(request,('item deleted'))
    return redirect('home')

def cross_off(request, list_id):
    item = taskdata.objects.get(pk=list_id)
    item.completed = True
    item.save()
      
    return redirect('home')


def uncross(request, list_id):
    item = taskdata.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

#view for editing or adding items
def edit(request,list_id):
    
#if request received from edit form submission
    if request.method == 'POST':
        #checks if form submission is from pre-existing item on list
        try:
            item = protocol.objects.get(pk=list_id)        
            form = ListForm(request.POST or None, instance=item)
            message="Item edited"
        #if is new item
        except:
            form = ListForm(request.POST or None)
            message="Item added"
            
        if form.is_valid():
            form.save()    
        
        #if form invalid
        else:
            message = 'Invalid form'

        messages.success(request,(message))
        return redirect('home')

#if request received from edit icon by item on home page list or add button
    else:
        #if item on list
        if list_id != '0':
            item = protocol.objects.get(pk=list_id)
            form = ListForm(request.POST or None, instance=item)
            removeFields(form,item)
            return render(request,'edit.html',{'form' : form, 'item' : item})
        #if request received from 'add' button on home page (passes id as 0)
        else:
            form = ListForm()
            return render(request,'edit.html',{'form' : form})


#view for editing or adding records in entities (eg persons, protocol types, tasks) 
# (this is very simliar code to def edit and so should be way to pass parameter to def than determines which form is run)
def entityForm(request,list_id,modelName):
    
#if request received from edit form submission
    if request.method == 'POST':
        #checks if form submission is from pre-existing record in model
        if modelName == 'persons':
            if list_id and list_id != "noId":
                item = persons.objects.get(pk=list_id)        
                form = personsForm(request.POST or None, instance=item)
                message="Person edited"
            #if is new item
            else:
                form = personsForm(request.POST or None)
                message="Person added"
            model = persons.objects.all

        elif modelName == 'protocoltype' or modelName == 'Protocol type':
            if list_id and list_id != "noId":
                item = protocoltype.objects.get(pk=list_id)        
                form = protocolTypeForm(request.POST or None, instance=item)
                message="protocl type edited"
            #if is new item
            else:
                form = protocolTypeForm(request.POST or None)
                message="protocol type added"
            model = protocoltype.objects.all

        elif modelName == 'task' or modelName == 'tasks':
            if list_id and list_id != "noId":
                item = task.objects.get(pk=list_id)        
                form = taskForm(request.POST or None, instance=item)
                message="task edited"
            #if is new item
            else:
                form = taskForm(request.POST or None)
                message="task added"
            model = task.objects.all

        elif modelName == 'protocol':
            if list_id and list_id != "noId":
                item = protocol.objects.get(pk=list_id)        
                form = ListForm(request.POST or None, instance=item)
                message="protocol edited"
            #if is new item
            else:
                form = ListForm(request.POST or None)
                message="protocol added"
            model = protocol.objects.all
            
        if form.is_valid():
            form.save()    
        
        #if form invalid
        else:
            errors = form.errors
            message = errors

        messages.success(request,(message))
        return render(request,'entities.html',{'model' : model,'modelName':modelName})

#if request received from entity page
    else:
        #if from item on list finds object instance and returns model appropriate form
        item=""
        if list_id != 'noId':
            model = str_to_class(modelName)
            item = model.objects.get(pk=list_id)
            if modelName == 'persons':
                form = personsForm(request.POST or None, instance=item)
            elif modelName == 'Protocol type' or modelName == 'protocoltype':
                form = protocolTypeForm(request.POST or None, instance=item)    
            elif modelName == 'task' or modelName == 'tasks':
                form = taskForm(request.POST or None, instance=item) 
            elif modelName == 'protocol' :
                form = ListForm(request.POST or None, instance=item) 
                   
        #if request received from 'add' button on entity page (passes id as 0)
        else:   
            if modelName == 'persons':
                form = personsForm(request.POST or None)
            elif modelName == 'Protocol type' or modelName == 'protocoltype':
                form = protocolTypeForm(request.POST or None)
            elif modelName == 'task' or modelName == 'tasks':
                form = taskForm(request.POST or None)
            elif modelName == 'protocol':
                form = ListForm(request.POST or None)
            else:
                form = taskForm(request.POST or None)
        
        return render(request,'edit.html',{'form' : form, 'item' : item})

def entities(request,modelName):
    if modelName == 'persons':
        model = persons.objects.all
    elif modelName == 'Protocol type':
        model = protocoltype.objects.all
    elif modelName == 'tasks':
        model = task.objects.all
    elif modelName == 'protocols':
        model = protocol.objects.all
    else:
        model = persons.objects.all
    return render(request,'entities.html',{'model' : model,'modelName':modelName})

def deleteInstance(request, list_id,modelName):
    
    if modelName == 'persons':
        item = persons.objects.get(pk=list_id)
        model = persons.objects.all
    elif modelName == 'protocoltype':
        item = protocoltype.objects.get(pk=list_id)
        model = protocoltype.objects.all
    elif modelName == 'protocol':
        item = protocol.objects.get(pk=list_id)
        model = protocol.objects.all 
    item.delete()
    messages.success(request,(modelName +' deleted'))
    return render(request,'entities.html',{'model' : model,'modelName':modelName})

#sets visible fields in form according to protocol type
def removeFields(form,protocol):
    visible_fields = protocol.visibleFields()
    visible_fields.append('type')
    invisible_fields = []
    #generates array of field names not to show on form
    for field in form.fields:
        if field not in visible_fields:
            invisible_fields.append(field)
    #removes fields not to show from field dictionary        
    for field in invisible_fields :
        if field in form.fields:
            form.fields.pop(field)

def logout_request(request):
    logout(request)
    return render (request,'index.html')

def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['nick@browndesign.co.uk',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('home')