from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employee.views import EmployeeAPIViewSet

router = DefaultRouter()
router.register(r'employee', EmployeeAPIViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
]
