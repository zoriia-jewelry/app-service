from django.db import models


class Order(models.Model):
    material = models.ForeignKey('Material', on_delete=models.PROTECT)
    client = models.ForeignKey('Client', on_delete=models.PROTECT)
    opened_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(auto_now=True, null=True)
    cancellation = models.TextField(null=True)
    discount = models.SmallIntegerField(null=True)
    loss = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    total_with_discount = models.DecimalField(max_digits=12, decimal_places=2, null=True)

    def __str__(self):
        return f'{self.material} - {self.client} - {self.opened_at}'

    class Meta:
        db_table = 'orders'


class OrderProduct(models.Model):
    order = models.ForeignKey('Order', on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    count = models.IntegerField()
    size = models.DecimalField(max_digits=12, decimal_places=2)
    notes = models.TextField()

    def __str__(self):
        return f'{self.order} - {self.product} - {self.count}'

    class Meta:
        db_table = 'order_products'
