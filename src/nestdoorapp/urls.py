from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('homepage', views.home_screen_view, name='home'),
    path('homepage/', views.home_screen_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.login_view, name='logout'),
    path('forum/', views.login_view, name='forum'),
    path('about/', views.login_view, name='about'),
    path('view1/', views.join, name='join'),
    path('view2/', views.name_list, name='name_list'),
]