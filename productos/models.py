from django.db import models

# Create your models here.

class CategoriaProds(models.Model):
    nombre = models.CharField(max_length=64)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
        
    def Meta(self):
        verbose_name = "categoriaProd"
        verbose_name_plural = "categoriasProd"
        

    def __str__(self):
        return self.nombre


class Productos(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=200)
    categorias = models.ForeignKey(CategoriaProds, on_delete=models.CASCADE)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='tienda')
    disponibilidad = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def Meta(self):
        verbose_name ="Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.titulo