from django.urls import path
from .views import home_page_view, test_api

urlpatterns = [
    path("", home_page_view, name="home"),
    path("api/test/", test_api, name="test_api"),
]
