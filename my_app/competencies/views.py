from django.db.models import fields
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import *
from .forms import *
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
    