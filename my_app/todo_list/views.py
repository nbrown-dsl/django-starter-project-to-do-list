from django.shortcuts import render, redirect
from .models import List, persons
from .forms import ListForm, personsForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,('Item added to list'))
            
    all_items = List.objects.all
    people = persons.objects.all
    return render(request,'home.html',{'all_items' : all_items,'people' : people})

# orders items alphabetically
def order(request):    
    # order items (minus sign for descending order) use eg [:5] at end of line to limit items returned
    people = persons.objects.all
    all_items = List.objects.order_by('item')
    
    return render(request,'home.html',{'all_items' : all_items,'people' : people})


def filter(request,query):
    people = persons.objects.all

    # filters across models using name of manaytomanyfield then attribute in related model, separated by __
    filtered_items = List.objects.filter(people__name = query)

    if len(filtered_items) > 0:
        messages.success(request,('Filtered by '+query))  
    elif query == "all":
        filtered_items = List.objects.all()
        messages.success(request,('All items'))  
    else:
        messages.success(request,('No filtered items')) 

    return render(request,'home.html',{'all_items' : filtered_items,'people' : people})   

def about(request):
    my_name ="Nick"
    return render(request,'about.html',{'name' : my_name})

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,('Item deleted'))
    return redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

#view for editing or adding items
def edit(request,list_id):
    
#if request received from edit form submission
    if request.method == 'POST':
        #checks if form submission is from pre-existing item on list
        try:
            item = List.objects.get(pk=list_id)        
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

#if request received from edit icon by item on home page list
    else:
        if list_id != '0':
            item = List.objects.get(pk=list_id)
            form = ListForm(request.POST or None, instance=item)
            return render(request,'edit.html',{'form' : form, 'item' : item})
        #if request received from 'add' button on home page (passes id as 0)
        else:
            form = ListForm()
            return render(request,'edit.html',{'form' : form})


#view for editing or adding persons 
# (this is very simliar code to def edit and so should be way to pass parameter to def than determines which form is run)
def editperson(request,list_id):
    
#if request received from edit form submission
    if request.method == 'POST':
        #checks if form submission is from pre-existing item on list
        try:
            item = persons.objects.get(pk=list_id)        
            form = personsForm(request.POST or None, instance=item)
            message="Person edited"
        #if is new item
        except:
            form = personsForm(request.POST or None)
            message="Person added"
            
        if form.is_valid():
            form.save()    
        
        #if form invalid
        else:
            message = 'Invalid form'

        messages.success(request,(message))
        return redirect('home')

#if request received from edit icon by item on home page list
    else:
        if list_id != '0':
            item = persons.objects.get(pk=list_id)
            form = personsForm(request.POST or None, instance=item)
            return render(request,'edit.html',{'form' : form, 'item' : item})
        #if request received from 'add' button on home page (passes id as 0)
        else:
            form = personsForm()
            return render(request,'edit.html',{'form' : form})