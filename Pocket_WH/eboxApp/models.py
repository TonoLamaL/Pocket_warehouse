from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Maestra(models.Model):
    ''' Tabla de creación de maestra de productos del inventario para el sistema'''
    nombre_producto = models.CharField(max_length=300)
    numero_sku = models.CharField(max_length=300)
    categoria = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.pk} (PK) | Nombre Producto: {self.nombre_producto}   |   Sku: {self.numero_sku}   |   Categoría: {self.categoria}'


class Recepcion(models.Model):
    ''' Tabla de ingresos de mercadería al sistema por recepciones (deberia sumar unidades al disponible en el sistema)'''
    num_contenedor = models.CharField(max_length=100)
    orden_compra = models.CharField(max_length=100, null = True)
    sku_in = models.ForeignKey(Maestra, on_delete=models.CASCADE)
    unidades_in = models.IntegerField()
    fecha_recepcion = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.pk} (PK) |Contenedor: {self.num_contenedor}   |   Sku: {self.sku_in}   |   Unidades: {self.unidades_in} '

    def save(self, *args, **kwargs):
        '''funcion para actualizar en linea las unidades segun las recepciones a la base de datos de inventario por sku'''
        super(Recepcion, self).save(*args, **kwargs)

        try:
            inventario = Inventario.objects.get(sku=self.sku_in)
            inventario.tot_unidades += self.unidades_in
            inventario.save()
        except ObjectDoesNotExist:
            Inventario.objects.create(sku=self.sku_in, tot_unidades=self.unidades_in) # no esta sirviendo ya que si no esta en la maestra no funciona - resolver

class Estados(models.Model):
    '''Tabla de estados'''
    estado = models.CharField(max_length=300)
    
    def __str__(self):
        return f'{self.pk} (PK) | Estado: {self.estado}'
    
class Salida(models.Model):
    ''' Tabla de ventas cargadas en el sistema que deben descontar unidades del inventario'''
    sku_out = models.ForeignKey(Maestra, on_delete=models.CASCADE, null=True)
    unidades_out = models.IntegerField()
    orden_venta = models.CharField(max_length=100)
    fecha_despacho = models.DateField(null=True)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE, null=True, default=1)
    
    def __str__(self):
        return f'{self.pk} (PK) | Sku: {self.sku_out}   |   Unidades: {self.unidades_out}  |  OC: {self.orden_venta} | Pk = {self.pk} | Pk = {self.estado}' 
    
def save(self, *args, **kwargs):
    '''funcion para actualizar en linea las unidades segun las salidas a la base de datos de inventario por sku '''
    try:
        inventario = Inventario.objects.get(sku=self.sku_out)
        if inventario.tot_unidades - self.unidades_out < 0:
            raise ValueError("No puedes preparar ese pedido, no te alcanzan las unidades, ajusta las unidades del pedido")
        inventario.unidades_reservadas += self.unidades_out
        inventario.unidades_disponibles = inventario.tot_unidades - inventario.unidades_reservadas
        inventario.save()
        super(Salida, self).save(*args, **kwargs)
    except ObjectDoesNotExist:
        Inventario.objects.create(sku=self.sku_out, tot_unidades=self.unidades_out, unidades_reservadas=self.unidades_out, unidades_disponibles=self.unidades_out)
        super(Salida, self).save(*args, **kwargs)
        
class Inventario(models.Model):
    ''' Tabla de inventario disponible en el sistema'''
    sku = models.ForeignKey(Maestra, on_delete=models.CASCADE, null=True)
    tot_unidades = models.IntegerField(null=True)
    unidades_reservadas = models.IntegerField(default=0)
    unidades_disponibles = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Si la instancia es nueva (no tiene primary key)
            self.unidades_disponibles = self.tot_unidades
        else:  # Si la instancia existe (tiene primary key)
            # Calcular las unidades disponibles restando las unidades reservadas
            self.unidades_disponibles = self.tot_unidades - self.unidades_reservadas
        super(Inventario, self).save(*args, **kwargs)


    
    def __str__(self):
        return f'{self.pk} (PK) | Sku: {self.sku}   |   Unidades: {self.tot_unidades} | Pk = {self.pk} |   Unidades: {self.unidades_reservadas} |   Unidades: {self.unidades_disponibles}'


    
