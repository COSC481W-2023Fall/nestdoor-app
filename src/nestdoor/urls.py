"""
URL configuration for nestdoor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
# from django.conf.urls import url
from nestdoorapp.views import *
from django.conf import settings
from django.conf.urls.static import static


from nestdoorapp.views import (
    home_screen_view,
    login_view,
    logout_view,
    forum_view,
    about_view,
)

urlpatterns = [
    path('', views.home_screen_view, name='home'),
    path('homepage/', views.home_screen_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.login_view, name='logout'),
    path('forum/', views.login_view, name='forum'),
    path('about/', views.login_view, name='about'),
    path('view1/', views.join, name='join'),
    path('view2/', views.name_list, name='name_list'),
]
