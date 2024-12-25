from django.urls import path
from .views import home_page_view, TestAPIView
from . import views

urlpatterns = [
    path("api/test/", TestAPIView.as_view(), name="test-api"),
    path("", views.dashboard, name='dashboard'),
    path('log/', views.log_study, name='log_study'),
    path('subjects/', views.subjects, name='subjects'),
]
