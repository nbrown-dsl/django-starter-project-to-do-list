from django.shortcuts import render
from django.views.generic import ListView
from .models import Usertask
from django.http import HttpResponseRedirect, HttpResponse




# # Create your views here.
class taskList(ListView):
    template_name = 'comps.html'
    model = Usertask
    # def get(self, request):
    #     # <view logic>
    #     return render(request,'competencies/comps.html')

def comps(request):

    usertasks = Usertask.objects.all()

    return render (request,'comps.html',{'userTasks':usertasks})

    


