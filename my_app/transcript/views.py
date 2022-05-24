from django.shortcuts import render

from django.contrib import messages

from transcript.functions.doc_output import mailmergeDoc
from transcript.functions.models import List
import json
import requests
#managebac API functions
from transcript.functions.data import *


def transcript(request):

    if request.method == 'POST':
        id = request.POST['id']

        studentObject = studentData(id)["student"]
        studentStart = studentObject["created_at"]

        years = studentTranscript(id, studentStart)

        # outputDoc(years)
        mailmergeDoc(years,studentObject)
        
                   
        messages.success(request,('Student Classes below and transcript doc generated'))
        return render(request,'transcript.html',{'years' : years,'student': studentObject})
    
    print ("request method: "+request.method)
    return render(request,'transcript.html',{'mbClasses' : mbClasses()['classes']})




def search(request):
    
    if request.method == 'POST' and len(request.POST['item'])>0:
        filterTerm = request.POST['item']
        filteredList = []

        for classes in mbClasses()["classes"]:
            if filterTerm in classes['name']:
                filteredList.append({'name':classes['name']})

        messages.success(request,('Courses containing '+filterTerm))
        return render(request,'transcript.html',{'mbClasses()' : filteredList})
    
    return render(request,'transcript.html',{'mbClasses' : mbClasses()['classes']})

def student(request):
    
    if request.method == 'POST':
        id = request.POST['id']

        studentObject = studentData(id)["student"]
        studentStart = studentObject["created_at"]

        years = studentTranscript(id, studentStart)

        # outputDoc(years)
        mailmergeDoc(years,studentObject)
        
                   
        messages.success(request,('Student Classes below and transcript doc generated'))
        return render(request,'transcript.html',{'years' : years,'student': studentObject})
    
    print ("request method: "+request.method)
    return render(request,'transcript.html')



#sort items alphabetically
def filterDone(request,state):
    filterSwitch = ''
    if state == 'done':
        filterSwitch = True
    else:
        filterSwitch = False
    filtered_items = List.objects.filter(completed=filterSwitch)
    return render(request,'transcript.html',{'all_items' : filtered_items})





