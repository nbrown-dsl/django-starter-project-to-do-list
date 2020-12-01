from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm,searchForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request,('Item added to list'))
            return render(request,'home.html',{'all_items' : all_items})

    else:

        all_items = List.objects.all
        return render(request,'home.html',{'all_items' : all_items})

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

def edit(request,list_id):

    if request.method == 'POST':
        items = List.objects.filter()

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request,('Item edited'))
            return redirect('home')

    else:

        item = List.objects.get(pk=list_id)
        return render(request,'edit.html',{'item' : item})

#called when search fomr submitted
#gets value entered in search form and uses to filter list
def search(request):

    if request.method == 'POST':
        
        form = searchForm(request.POST or None)
        if form.is_valid():
            searchTerm = form.cleaned_data.get("searchTerm")
            messages.success(request,str("results filtered by '"+searchTerm+"'"))
            filtered_items = List.objects.filter(item__contains=searchTerm)
            return render(request,'home.html',{'all_items' : filtered_items})

    
    all_items = List.objects.all
    return render(request,'home.html',{'all_items' : all_items})