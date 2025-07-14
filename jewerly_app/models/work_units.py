from django.db import models


class WorkUnit(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT)
    order = models.ForeignKey('Order', on_delete=models.PROTECT)
    issued_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(auto_now=True, null=True)
    issued = models.DecimalField(max_digits=17, decimal_places=5)
    returned = models.DecimalField(max_digits=17, decimal_places=5, null=True)
    loss = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    returned_with_loss = models.DecimalField(max_digits=17, decimal_places=2, null=True)

    def __str__(self):
        return f'{str(self.issued_at)} - {self.employee.full_name}'

    class Meta:
        db_table = 'work_units'
