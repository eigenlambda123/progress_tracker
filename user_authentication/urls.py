# user_authentication/urls.py
from django.urls import path
from . import views

urlpatterns = [
   path('login/', views.login_view, name='login'),
   path('register/', views.register, name='register'),
   path('logout/', views.user_logout, name='logout'),
]
