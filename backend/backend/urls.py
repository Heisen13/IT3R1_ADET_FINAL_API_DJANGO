from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from attendance.views import AttendanceViewSet

router = DefaultRouter()
router.register(r'attendance', AttendanceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]