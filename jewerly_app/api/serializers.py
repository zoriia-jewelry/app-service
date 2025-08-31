from rest_framework import serializers
from jewerly_app.models import *


class EmployeeReadSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='full_name', read_only=True)
    phone = serializers.CharField(source='phone_number', read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'phone']


class EmployeeUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='full_name')
    phone = serializers.CharField(source='phone_number')

    class Meta:
        model = Employee
        fields = ['name', 'phone', 'is_archived']
