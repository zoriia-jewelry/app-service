from django.contrib import admin
from django.urls import path
from jewerly_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
]
