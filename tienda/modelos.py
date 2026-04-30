from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)

    class Meta:
        app_label = 'tienda'

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()

    class Meta:
        app_label = 'tienda'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()

    class Meta:
        app_label = 'tienda'

    def __str__(self):
        return self.nombre
