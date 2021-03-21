from django.urls import path
# from .views import taskList
from . import views


urlpatterns = [
    
    # path('comps/', taskList.as_view()),
    path('comps/', views.comps, name='comps'),
    path('editInstance/', views.editInstance, name='editInstance'),
    
 ]