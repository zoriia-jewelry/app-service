from django.urls import path
from jewerly_app import views

urlpatterns = [
    path('employees/', views.EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view(), name='employee-detail'),
]