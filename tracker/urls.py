from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudyLogViewSet, TrackerViewSet, SubjectViewSet
from .import views

# Create a router for the ViewSets
router = DefaultRouter()
router.register(r'studylog', StudyLogViewSet, basename='studylog')
router.register(r'tracker', TrackerViewSet, basename='tracker')
router.register(r'subject', SubjectViewSet, basename='subject')

urlpatterns = [
   
    path("", views.dashboard, name='dashboard'),
    path('log/', views.log_study, name='log_study'),
    path('subjects/', views.subjects, name='subjects'),

    # api
     path("api/", include(router.urls)),
]
