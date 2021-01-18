from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('delete/<list_id>',views.delete,name='delete'),
    path('cross_off/<list_id>',views.cross_off,name='cross_off'),
    path('uncross/<list_id>',views.uncross,name='uncross'),
    path('edit/<list_id>',views.edit,name='edit'),
    path('entityForm/<list_id>/<modelName>/',views.entityForm,name='entityForm'),
    path('filter/<query>',views.filter,name='filter'),
    path('order',views.order,name='order'),
    path('entities/<modelName>',views.entities,name='entities')
]
