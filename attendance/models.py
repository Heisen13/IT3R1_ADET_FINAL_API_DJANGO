from django.db import models

class AttendanceRecord(models.Model):
    tag_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)