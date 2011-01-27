from django.contrib import admin
from models import Product, Currency, Manufacturer, Order, Cart

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Currency, CurrencyAdmin)

class ManufacturerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Manufacturer, ManufacturerAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Order, OrderAdmin)

class CartAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cart, CartAdmin)
