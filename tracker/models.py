from django.db import models
from django.conf import settings

# Create your models here.
class Tracker(models.Model):
    name = models.CharField(max_length=100)
    age = models

class StudyLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    time_spent = models.FloatField()  # In hours
    notes = models.TextField(blank=True, null=True)
    date_logged = models.DateTimeField(auto_now_add=True)


class Subject(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
