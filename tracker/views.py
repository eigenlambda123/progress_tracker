from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tracker
from .serializers import TrackerSerializer

class TestAPIView(APIView):
    def get(self, request):
        data = Tracker.objects.all()
        serializer = TrackerSerializer(data, many=True)
        return Response(serializer.data)


def home_page_view(request):
    return HttpResponse("Hello, World!")
