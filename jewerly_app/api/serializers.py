from rest_framework import serializers
from jewerly_app.models import *


class EmployeeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='full_name')
    phone = serializers.CharField(source='phone_number')

    class Meta:
        model = Employee
        fields = ['id', 'name', 'phone', 'is_archived']
