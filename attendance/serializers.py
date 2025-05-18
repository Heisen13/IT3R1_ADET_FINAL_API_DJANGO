from rest_framework import serializers
from .models import AttendanceRecord

class AttendanceSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = AttendanceRecord
        fields = '__all__'
