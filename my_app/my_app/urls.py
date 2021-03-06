
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views


urlpatterns = [
    path('',include('todo_list.urls')),
    path('admin/', admin.site.urls),
    path('login/',views.LoginView)
    
]
