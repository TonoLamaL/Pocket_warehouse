from django.db import models

class Maestra(models.Model):
    ''' Tabla de creación de maestra de productos del inventario para el sistema'''
    nombre_producto = models.CharField(max_length=300)
    numero_sku = models.IntegerField()
    categoria = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.pk} (PK) | Nombre Producto: {self.nombre_producto}   |   Sku: {self.numero_sku}   |   Categoría: {self.categoria}'

class Recepcion(models.Model):
    ''' Tabla de ingresos de mercadería al sistema por recepciones (deberia sumar unidades al disponible en el sistema)'''
    num_contenedor = models.CharField(max_length=100)
    sku_in = models.ForeignKey(Maestra, on_delete=models.CASCADE)
    unidades_in = models.IntegerField()
    
    def __str__(self):
        return f'{self.pk} (PK) |Contenedor: {self.num_contenedor}   |   Sku: {self.sku_in}   |   Unidades: {self.unidades_in} '

class Salida(models.Model):
    ''' Tabla de ventas cargadas en el sistema que deben descontar unidades del inventario'''
    sku_out = models.ForeignKey(Maestra, on_delete=models.CASCADE)
    unidades_out = models.IntegerField()
    orden_venta = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.pk} (PK) | Sku: {self.sku_out}   |   Unidades: {self.unidades_out}  |  OC: {self.orden_venta} | Pk = {self.pk}'

class Inventario(models.Model):
    ''' Tabla de inventario disponible en el sistema'''
    sku = models.ForeignKey(Maestra, on_delete=models.CASCADE, null=True)
    tot_unidades = models.IntegerField(null=True)
    
    def __str__(self):
        return f'{self.pk} (PK) | Sku: {self.sku}   |   Unidades: {self.tot_unidades} | Pk = {self.pk}'
    
