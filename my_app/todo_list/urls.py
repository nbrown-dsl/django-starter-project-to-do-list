from django.urls import path, include
from . import views
# from .views import taskList

# from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home,name='home'), 
    path('accounts/', include('allauth.urls')),
    path('logout', views.logout_request, name='logout'),
    path('home',views.home,name='home'),
    path('home/<nameFilter>',views.home,name='home'),
    path('about',views.about,name='about'),
    path('delete/<list_id>',views.delete,name='delete'),
    path('crossoff/<list_id>',views.crossoff,name='crossoff'),
    path('uncross/<list_id>',views.uncross,name='uncross'),
    path('edit/<list_id>',views.edit,name='edit'),
    path('protocolAdd/<type>',views.protocolAdd,name='protocolAdd'),
    path('entityForm/<list_id>/<modelName>/',views.entityForm,name='entityForm'),
    path('entities/<modelName>',views.entities,name='entities'),
    path('deleteInstance/<list_id>/<modelName>/',views.deleteInstance,name='deleteInstance'),
    path('email',views.email,name='email'),
    path('cross/',views.cross,name='cross'),
    #comp views
    # path('persons_list/', taskList.as_view()),

    
]
