from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    article_code = models.CharField(max_length=255)
    photo_url = models.URLField(max_length=500, null=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.article_code

    class Meta:
        db_table = 'products'


class Material(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'materials'
