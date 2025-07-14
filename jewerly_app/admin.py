from django.contrib import admin
from jewerly_app.models import products_materials, price_lists, clients, orders, employees

admin.site.register(products_materials.Product)
admin.site.register(products_materials.Material)
admin.site.register(price_lists.PriceList)
admin.site.register(price_lists.PriceListEntry)
admin.site.register(clients.Client)
admin.site.register(clients.ClientMaterial)
admin.site.register(orders.Order)
admin.site.register(orders.OrderProduct)
admin.site.register(employees.Employee)
admin.site.register(employees.EmployeeOrder)
