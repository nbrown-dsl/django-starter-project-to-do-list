
from django.contrib import admin
from django.urls import path, include

# from django.contrib.auth import views


urlpatterns = [
    path('',include('todo_list.urls')),
    path('',include('competencies.urls')),
    path('admin/', admin.site.urls),
    # path('login/',views.LoginView)
    # path('login/',
    # views.LoginView, {'template_name': 'login.html'}
    # ),
    # path('logout/',
    # views.LogoutView, {'next_page': '/login/'}
    # ),
    
]
