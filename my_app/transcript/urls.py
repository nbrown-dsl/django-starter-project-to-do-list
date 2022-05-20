from django.urls import path
# from .views import taskList
from . import views


urlpatterns = [
    
    # path('comps/', taskList.as_view()),
    path('', views.transcript,name='transcript'), 
    path('transcript/', views.transcript, name='transcript'),
    path('student/', views.student, name='student'),
    # path('mycomps/', views.mycomps, name='mycomps'),
    # path('comps/<object>/', views.saveForm, name='saveForm'),
    # path('renderForm/<object>/', views.renderForm, name='renderForm'),
    # path('deleteInstance/<objectID>/', views.deleteInstance, name='deleteInstance'),
    # path('importCSV/<object>/',views.importCSV,name='importCSV'),
    # path('exportCSV/<entityName>/',views.exportCSV,name='exportCSV'),
    # path('gradeChange/',views.gradeChange,name='gradeChange'),
    # path('profile/',views.profile,name='profile'),
    # path('allcomps/',views.allcomps,name='allcomps'),
    # path('vote/',views.vote,name='vote'),
    # path('skilledUsers/',views.skilledUsers,name='skilledUsers'),
 
 ]