from django.contrib import admin
from .models import AttendanceRecord

@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('tag_id', 'name', 'timestamp')
    search_fields = ('tag_id', 'name')
