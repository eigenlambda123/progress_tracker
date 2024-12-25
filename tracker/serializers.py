from rest_framework import serializers
from .models import Tracker 
from .models import StudyLog

class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = '__all__'

class StudyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyLog
        fields = '__all__'