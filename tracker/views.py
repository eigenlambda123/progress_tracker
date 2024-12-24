from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def test_api(request):
    return Response({"message": "Hello, API!"})


def home_page_view(request):
    return HttpResponse("Hello, World!")
