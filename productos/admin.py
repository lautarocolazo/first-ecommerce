from django.contrib import admin
from .models import CategoriaProds, Productos
# Register your models here.

class CategoriaProdsAdmin(admin.ModelAdmin):
    readonly_field = ("created", "updated")

class ProductosAdmin(admin.ModelAdmin):
    readonly_field = ("created", "updated")

admin.site.register(CategoriaProds, CategoriaProdsAdmin)
admin.site.register(Productos, ProductosAdmin)

