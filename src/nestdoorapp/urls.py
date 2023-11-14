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
    path('login/', views.login_view, name='login'),
    path('accounts/password_reset/', views.password_reset, name='password_reset'),
    path('accounts/password_reset_done/', views.password_reset_done, name='password_reset_done'),

    path('forum/', views.forum_view, name='forum'),
    path('edit/', views.edit_post, name="edit"),
    path('about/', views.about_view, name='about'),
    path('user/', views.bad_profile_view, name='bad_profile_view'),
    path('user/<int:user_id>', views.user_profile_view, name='user_profile'),
    # path('userpost/', views.user_post_view, name='user_post'),
    path('userpost/<str:pk>', views.user_post_view, name='user_post'),
    path('deleteComment/<str:pk>',
         views.deleteComment, name='deleteComment'),
    path('view1/', views.join, name='join'),
    path('view2/', views.name_list, name='name_list'),
]
    #reset confirm/done/uidb64