from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from jewerly_app.api.pagination import PaginationPageSize
from rest_framework import generics
from jewerly_app.api import serializers
from jewerly_app.models import *


class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['is_archived']
    pagination_class = PaginationPageSize
    ordering = ['id']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.EmployeeReadSerializer
        return serializers.EmployeeUpdateSerializer


class EmployeeDetailView(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.EmployeeReadSerializer
        return serializers.EmployeeUpdateSerializer


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['is_archived']
    search_fields = ['name', 'article_code']
    ordering = ['id']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.ProductReadSerializer
        return serializers.ProductUpdateSerializer


class ProductDetailView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.ProductReadSerializer
        return serializers.ProductUpdateSerializer
