from django.db import models
from .products_materials import Material


class PriceList(models.Model):
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return str(self.start_date)

    class Meta:
        db_table = 'price_lists'


class PriceListEntries(models.Model):
    price_list = models.ForeignKey(PriceList, on_delete=models.PROTECT)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return str(self.price_list)

    class Meta:
        db_table = 'price_list_entries'