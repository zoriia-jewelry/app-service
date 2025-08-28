from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import generics
from jewerly_app.api import serializers
from jewerly_app.models import *


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['is_archived']
    ordering = ['id']


class EmployeeDetail(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
