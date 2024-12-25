from django.shortcuts import render, redirect # new
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Subject, Tracker, StudyLog
from .serializers import TrackerSerializer, StudyLogSerializer


# Views

def dashboard(request):
    study_logs = StudyLog.objects.filter(user=request.user)
    return render(request, 'tracker/dashboard.html', {'study_logs': study_logs})


def log_study(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        time_spent = request.POST['time_spent']
        notes = request.POST.get('notes', '')
        StudyLog.objects.create(user=request.user, subject=subject, time_spent=time_spent, notes=notes)
        return redirect('dashboard')
    return render(request, 'tracker/log_study.html')

def subjects(request):
    subjects = Subject.objects.filter(user=request.user)
    return render(request, 'tracker/subjects.html', {'subjects': subjects})

def home_page_view(request):
    return HttpResponse("Hello, World!")

# API

class TestAPIView(APIView):
    def get(self, request):
        data = Tracker.objects.all()
        serializer = TrackerSerializer(data, many=True)
        return Response(serializer.data)

class StudyLogViewSet(ModelViewSet):
    queryset = StudyLog.objects.all()
    serializer_class = StudyLogSerializer

