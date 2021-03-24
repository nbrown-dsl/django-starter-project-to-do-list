from django.urls import path
# from .views import taskList
from . import views


urlpatterns = [
    
    # path('comps/', taskList.as_view()),
    
    path('comps/', views.comps, name='comps'),
    path('comps/<object>/', views.saveForm, name='saveForm'),
    path('renderForm/<object>/', views.renderForm, name='renderForm'),
    path('deleteInstance/<int:objectID>/', views.deleteInstance, name='deleteInstance'),
 
 ]