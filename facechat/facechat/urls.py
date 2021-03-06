"""facechat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.generic import TemplateView
from boards import views
#from facechat.boards.views import regi_input

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.index, name='index'),
     #path('home/',views.home),
    url(r'^home/',views.home,name='home'),
     path('test/', views.test,name='test'),
     path('profile/',views.profile,name='profile'),
    
    
    path('loginform/',views.loginform,name='loginform'),

    #path('logout/',views.loginform,name='logout'),

    path('login',views.login,name='login'),
    
    
    path('register/',views.register,name='register'),
    path('register/regi_input',views.regi_input,name='regi_input')
]
