from django.db import models


class Maestra(models.Model):
    nombre_producto = models.CharField(max_length=300)
    numero_sku = models.IntegerField()
    categoria = models.CharField(max_length=300)

    def __str__(self):
        return f'Nombre Producto: {self.nombre_producto}   /   Sku: {self.numero_sku}   /   Categoría: {self.categoria}'

class Inventario(models.Model):
    #producto = models.ForeignKey(Maestra, on_delete=models.CASCADE)
    sku = models.ForeignKey(Maestra, on_delete=models.CASCADE)
    unidades = models.IntegerField()
    
    def __str__(self):
        return f'Sku: {self.sku}   /   Unidades: {self.unidades}'

class Recepcion(models.Model):
    num_contenedor = models.CharField(max_length=100)
    sku_in = models.ForeignKey(Maestra, on_delete=models.CASCADE)
    unidades_in = models.IntegerField()
    
    def __str__(self):
        return f'Contenedor: {self.num_contenedor}   /   Sku: {self.sku_in}   /   Unidades: {self.unidades_in}'

class Salida(models.Model):
    sku_out = models.ForeignKey(Maestra, on_delete=models.CASCADE)
    unidades_out = models.IntegerField()
    
    def __str__(self):
        return f'Sku: {self.sku_out}   /   Unidades: {self.unidades_out}'