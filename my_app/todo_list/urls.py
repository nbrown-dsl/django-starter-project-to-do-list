from django.urls import path, include
from . import views
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')), # <--
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('logout', views.logout_request, name='logout'),
    path('accounts/', include('allauth.urls')),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('delete/<list_id>',views.delete,name='delete'),
    path('cross_off/<list_id>',views.cross_off,name='cross_off'),
    path('uncross/<list_id>',views.uncross,name='uncross'),
    path('edit/<list_id>',views.edit,name='edit'),
    path('protocolAdd/<type>',views.protocolAdd,name='protocolAdd'),
    path('entityForm/<list_id>/<modelName>/',views.entityForm,name='entityForm'),
    path('filter/<query>/<model>',views.filter,name='filter'),
    # path('order',views.order,name='order'),
    path('entities/<modelName>',views.entities,name='entities'),
    path('deleteInstance/<list_id>/<modelName>/',views.deleteInstance,name='deleteInstance'),
    path('email',views.email,name='email'),

    
]
