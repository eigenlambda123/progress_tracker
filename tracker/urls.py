from django.urls import path
from .views import home_page_view, TestAPIView

urlpatterns = [
    path("", home_page_view, name="home"),
    path("api/test/", TestAPIView.as_view(), name="test-api"),
]
