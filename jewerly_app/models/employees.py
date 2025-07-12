from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'employees'


class EmployeeOrder(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT)
    order = models.ForeignKey('Order', on_delete=models.PROTECT)

    def __str__(self):
        return f'orders: {self.employee.full_name}'

    class Meta:
        db_table = 'employee_orders'
