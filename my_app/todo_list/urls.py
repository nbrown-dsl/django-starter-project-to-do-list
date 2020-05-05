from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('delete/<list_id>',views.delete,name='delete'),
    path('cross_off/<list_id>',views.cross_off,name='cross_off'),
    path('uncross/<list_id>',views.uncross,name='uncross'),
    path('edit/<list_id>',views.edit,name='edit'),
    path('search',views.search,name='search'),
    path('sortAlpha',views.sortAlpha,name='sortAlpha'),
    path('filterDone/<state>',views.filterDone,name='filterDone'),
    
    

]
