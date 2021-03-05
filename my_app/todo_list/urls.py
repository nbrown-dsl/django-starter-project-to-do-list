from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf.urls import url
# from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home,name='home'), # <--
    # path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('logout', views.logout_request, name='logout'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('delete/<list_id>',views.delete,name='delete'),
    path('crossoff/<list_id>',views.crossoff,name='crossoff'),
    path('uncross/<list_id>',views.uncross,name='uncross'),
    path('edit/<list_id>',views.edit,name='edit'),
    path('protocolAdd/<type>',views.protocolAdd,name='protocolAdd'),
    path('entityForm/<list_id>/<modelName>/',views.entityForm,name='entityForm'),
    # path('filter/<query>/<model>',views.filter,name='filter'),
    # path('order',views.order,name='order'),
    path('entities/<modelName>',views.entities,name='entities'),
    path('deleteInstance/<list_id>/<modelName>/',views.deleteInstance,name='deleteInstance'),
    path('email',views.email,name='email'),
    path('clear',views.clear,name='clear'),
    url(r'^cross/$', views.cross, name='cross'),

    
]
