from django.db.models import fields
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import *
from .forms import TaskForm
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import modelform_factory




# # Create your views here.
# class taskList(ListView):
#     template_name = 'comps.html'
#     model = Usertask
    # def get(self, request):
    #     # <view logic>
    #     return render(request,'competencies/comps.html')

def comps(request):
    objectList = []
    for table in entity.__subclasses__():
        objectList.append({'name':table.__name__,'objects':table.objects.all()})


    return render (request,'comps.html',{'objectDic':objectList})

#for saving form submissions    
def saveForm(request,object):
    #if object is id ie is pre-exisitng instance      
    try:
        objectID = int(object)
        for table in entity.__subclasses__():
                for instance in table.objects.all():
                    if instance.id == objectID:
                        form = TaskForm(request.POST or None, instance = instance)

                        if form.is_valid():
                            form.save()
            
    
    #if object is name of model, ie new instance            
    except:
        for table in entity.__subclasses__():
                if table.__name__ == str(object):
                    print (object)
                
    return redirect ('comps')
   

#for rendering forms
def renderForm(request,object):
    #for rendering bound form from exisitng instance
    try: #checks if object is object id (ie convertable to integer)
        objectID = int(object)
        for table in entity.__subclasses__():
                    for instance in table.objects.all():
                        if instance.id == objectID:
                            editInstance = table.objects.get(pk=object)
                            formObject = modelform_factory(table,fields=("__all__"))
                            form = formObject(instance=editInstance)

    #for rendering unbound form for adding new instance
    except:
        for table in entity.__subclasses__():
                if table.__name__ == str(object):
                    form = modelform_factory(table,fields=("__all__"))

    return render (request,'renderForm.html',{'formObject':form, 'object': object})
    