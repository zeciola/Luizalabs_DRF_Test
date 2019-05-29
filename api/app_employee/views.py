from .models import Employee
from .serializers import EmployeeSerializer
from django.shortcuts import render
from rest_framework import viewsets


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
