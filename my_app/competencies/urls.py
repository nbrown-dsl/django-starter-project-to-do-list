from django.urls import path
from .views import taskList




urlpatterns = [
    
    path('comps/', taskList.as_view()),
    
 ] # <--