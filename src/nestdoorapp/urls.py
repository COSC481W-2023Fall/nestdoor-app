from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_screen_view, name="home"),
    path('view1/', views.join, name='join'),
    path('view2/', views.name_list, name='name_list'),
    
]