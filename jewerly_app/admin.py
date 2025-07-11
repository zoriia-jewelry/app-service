from django.contrib import admin
from jewerly_app.models import products_materials, price_lists

admin.site.register(products_materials.Product)
admin.site.register(products_materials.Material)
admin.site.register(price_lists.PriceList)
admin.site.register(price_lists.PriceListEntries)
