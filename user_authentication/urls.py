# user_authentication/urls.py
from django.urls import path
from . import views

urlpatterns = [
   # authentication
   path('login/', views.login_view, name='login'),
   path('register/', views.register, name='register'),
   path('logout/', views.user_logout, name='logout'),

   # profile
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
]
