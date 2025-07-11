from django.contrib import admin
from jewerly_app.models import products_materials, price_lists, clients

admin.site.register(products_materials.Product)
admin.site.register(products_materials.Material)
admin.site.register(price_lists.PriceList)
admin.site.register(price_lists.PriceListEntry)
admin.site.register(clients.Client)
admin.site.register(clients.ClientMaterial)
admin.site.register(clients.MaterialAuditEntry)
