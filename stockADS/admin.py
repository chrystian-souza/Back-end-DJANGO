from django.contrib import admin
from .models import Products, Categorias

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','in_stock']
    list_filter = ['in_stock']
    # list_editable = ['size']
    search_fields = ['name']


admin.site.register(Products, ProductsAdmin)
admin.site.register(Categorias)
                    

# Register your models here.
