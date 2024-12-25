from rest_framework import serializers
from .models import Tracker, StudyLog, Subject


class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = '__all__'

class StudyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyLog
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'