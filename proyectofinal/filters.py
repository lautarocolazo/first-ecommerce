import django_filters

from productos.models import *

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = CategoriaProds
        fields = "__all__"