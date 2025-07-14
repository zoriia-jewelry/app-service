from django.db import models


class Client(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'clients'


class ClientMaterial(models.Model):
    client = models.ForeignKey('Client', on_delete=models.PROTECT)
    material = models.ForeignKey('Material', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f'client: {self.client.full_name} - material: {self.material.name}'

    class Meta:
        db_table = 'client_materials'
