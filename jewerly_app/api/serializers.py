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


class ProductReadSerializer(serializers.ModelSerializer):
    article = serializers.CharField(source='article_code', read_only=True)
    picture_url = serializers.URLField(source='photo_url', read_only=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'article', 'picture_url', 'is_archived']


class ProductUpdateSerializer(serializers.ModelSerializer):
    article = serializers.CharField(source='article_code')
    picture_url = serializers.URLField(source='photo_url', required=False, allow_null=True)

    class Meta:
        model = Product
        fields = ['name', 'article', 'picture_url', 'is_archived']
