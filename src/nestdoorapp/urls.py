from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_screen_view, name='home'),
    path('admin/', admin.site.urls),
    path('homepage/', views.home_screen_view, name='home'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('forum/', views.forum_view, name='forum'),
    path('about/', views.about_view, name='about'),
    path('view1/', views.join, name='join'),
    path('view2/', views.name_list, name='name_list'),
]