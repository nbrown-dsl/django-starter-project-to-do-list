
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('accounts.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html')),
    path('',include('competencies.urls')),
    path('',include('todo_list.urls')),
    path('',include('transcript.urls')),
    
    
]
