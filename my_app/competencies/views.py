from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import *
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse




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

    
def editInstance(request,objectId):

    if request.method == 'POST':
        pass

    else:
    
        for table in entity.__subclasses__():
            for instance in table.objects.all():
                if instance.id == int(objectId):
                    object = table.objects.get(pk=objectId)
                    formObject = TaskForm(request.POST or None, instance=object)


    return render (request,'editInstance.html',{'formObject':formObject})

