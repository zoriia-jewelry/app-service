from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    article_code = models.CharField(max_length=255)
    photo_url = models.URLField(max_length=500, null=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.article_code}'

    class Meta:
        db_table = 'products'


class Material(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'materials'


class MaterialAuditRecord(models.Model):
    # user
    client = models.ForeignKey('Client', on_delete=models.PROTECT, null=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'user - {str(self.date)}'

    class Meta:
        db_table = 'material_audit_records'


class MaterialAuditRecordRow(models.Model):
    material = models.ForeignKey('Material', on_delete=models.PROTECT, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    material_audit_record = models.ForeignKey('MaterialAuditRecord', on_delete=models.PROTECT)

    def __str__(self):
        material_name = self.material.name if self.material else 'Вартість'
        return f'{material_name} - {self.amount}'

    class Meta:
        db_table = 'material_audit_record_rows'
