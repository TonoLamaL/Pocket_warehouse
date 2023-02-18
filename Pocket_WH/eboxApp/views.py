from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from eboxApp.models import *
from eboxApp.forms import *
from django.contrib import messages

def index(request):
    ''' Página de inicio '''
    return render (request, 'eboxApp/index.html')


# MAESTRA 

def maestra(request):
    ''' Formulario para crear nuevos productos en la maestra de productos - te llevo a una ventana distinta con boton volver'''
    if request.method == 'POST': # si existe un post
        maestra_prod = MaestraForm(data=request.POST)
        print (maestra_prod)
        
        # una validacion que pide django ({% csrf_token %}) en el html
        if maestra_prod.is_valid():
            informacion = maestra_prod.cleaned_data
            nuevo_producto = Maestra(nombre_producto = informacion['nombre_producto'], numero_sku = informacion['numero_sku'], categoria = informacion['categoria']) # son los argumentos de la clase y la guardo en el objeto     
            nuevo_producto.save()
            return render(request, 'eboxApp/windowsConfirm.html') # una vez que se guardo que retorne a la pagina de confrimación, y desde la confirmacion window hice un html que me retorna a inicio
    
    else:
        maestra_prod = MaestraForm()
    
    return render(request, 'eboxApp/maestra.html', {'maestra_prod':maestra_prod}) # si hay campos vacios estamos en esta html -> este link dice quien toma la funcion de form 


def buscarProducto(request):
    ''' Formulario para buscar un producto en especifico por su nombre - te llevo a una ventana distinta con boton volver'''
    if request.method == 'GET': # si existe un post
        busqueda = request.GET['nombre_producto']
        #busqueda = busqueda.lower()
        producto = Maestra.objects.filter(nombre_producto = busqueda)
        
        return render(request, 'eboxApp/wMaestra_list.html', {'producto':producto , 'busqueda':busqueda })
    
def buscarMaestra(request):
    ''' Boton de busqueda completa de la maestra con respuesta en una lista - te llevo a una ventana distinta con boton volver'''
    if request.method == 'GET': # si existe un post
        producto = Maestra.objects.all()
        
        return render(request, 'eboxApp/wMaestra_full.html', {'producto':producto })


# RECEPCIÓN

def recepcion(request):
    " Formulario para crear una recepción que tiene que ingresar productos al inventario"
    if request.method == 'POST': # si existe un post
        recepcion_prod = RecepcionForm(data=request.POST)
        print (recepcion_prod)
        
        # una validacion que pide django ({% csrf_token %})
        if recepcion_prod.is_valid():
            informacion = recepcion_prod.cleaned_data
            nueva_recepcion = Recepcion(num_contenedor = informacion['num_contenedor'], sku_in = informacion['sku_in'], unidades_in = informacion['unidades_in']) # son los argumentos de la clase y la guardo en el objeto     
            nueva_recepcion.save()
            #nuevo_registro_in = Inventario(result = tot_unidades + informacion['unidades_in'], sku = informacion['sku_in'], )
            #nuevo_registro_in.save()
            return render(request, 'eboxApp/windowsConfirm.html') # una vez que se guardo que retorne a la pagina de confrimación, y desde la confirmacion window hice un html que me retorna a inicio

            

    else:
        recepcion_prod = RecepcionForm()
    
    return render(request, 'eboxApp/recepcion.html', {'recepcion_prod':recepcion_prod})

def buscarRecepcion(request):
    ''' Boton de busqueda completa de las recepciones con respuesta en una lista - te llevo a una ventana distinta con boton volver'''
    if request.method == 'GET': # si existe un post
        recepciones = Recepcion.objects.all()
        
        return render(request, 'eboxApp/wRecepcion_full.html', {'recepciones':recepciones })

# CREACIÓN DE ORDENES
def egreso(request):
    " Formulario para crear un egreso que tiene que salir productos al inventario"
    if request.method == "POST":
        form = EgresoForm(data=request.POST)
        print (form)
    
        if form.is_valid():
            sku_out = form.cleaned_data["sku_out"]
            unidades_out = form.cleaned_data["unidades_out"]
            orden_venta = form.cleaned_data["orden_venta"]

            try:
                inventario = Inventario.objects.get(sku=sku_out)
                if inventario.tot_unidades - unidades_out < 0:
                    messages.error(request, "No puedes preparar ese pedido. Las unidades que pides no alcanzan, ajusta las unidades.")
                    return render(request, "eboxApp/egreso.html", {"form": form})
                else:
                    Salida.objects.create(sku_out=sku_out, unidades_out=unidades_out, orden_venta=orden_venta)
                    inventario.tot_unidades -= unidades_out
                    inventario.save()
                    return render(request, 'eboxApp/windowsConfirm.html') # una vez que se guardo que retorne a la pagina de confrimación, y desde la confirmacion window hice un html que me retorna a inicio
            except ObjectDoesNotExist:
                Inventario.objects.create(sku=sku_out, tot_unidades=unidades_out)
                Salida.objects.create(sku_out=sku_out, unidades_out=unidades_out, orden_venta=orden_venta)
                return render(request, 'eboxApp/windowsConfirm.html') # creo que esto no aplica porque no puedo crear egresos de prooductos que no existen en la maestra, y me estan quedando ahi cuando estan en cero. Si los elimino cuando llegan a 0 podría ser util
    else:
        form = EgresoForm()

    return render(request, "eboxApp/egreso.html", {"form": form})

def buscarEgreso(request):
    ''' Boton de busqueda completa de las ordenes de compra con respuesta en una lista - te llevo a una ventana distinta con boton volver'''
    if request.method == 'GET': # si existe un post
        salidas = Salida.objects.all()
        
        return render(request, 'eboxApp/wEgreso_full.html', {'salidas':salidas })



# INVENTARIO


def stock_en_linea(request):
    '''funcion para revisar el stock en linea - esta es solo para mostrar - las funciones son
    parte de las clases Recepcion y Salida '''
    inventarios = Inventario.objects.all()
    return render(request, 'eboxApp/stock_en_linea.html', {'inventarios': inventarios})
 
 
 # FUNCIONES DE USO INTENRO AQUI ABAJO
'''
IR AL SHELL DE DJANGO Y EJECUTAR

from eboxApp.views import migrar_inventario, actualizar_inventariof

migrar_inventario()
actualizar_inventario()
'''

def actualizar_inventario():#agregar request si quiero que sea desde una web:
    '''funcion para actualizar el inventario en unidades - lo necesitaba porque la ultima clase que cree fue inventario'''
    inventario = Inventario.objects.all()
    for inv in inventario:
        # Aquí se actualiza el valor de tot_unidades para cada registro de inventario
        inv.tot_unidades = inv.sku.recepcion_set.aggregate(models.Sum('unidades_in'))['unidades_in__sum'] - inv.sku.salida_set.aggregate(models.Sum('unidades_out'))['unidades_out__sum']
        inv.save()

    #return HttpResponse ('eboxApp/actualizar_inventario.html')

def migrar_inventario():
    '''Función que actualiza el inventario a partir de los registros en las tablas de Recepcion y Salida
    - lo necesitaba porque la ultima clase que cree fue inventario'''

    # Recorrer los objetos de Recepcion
    for recepcion in Recepcion.objects.all():
        sku = recepcion.sku_in
        unidades = recepcion.unidades_in
        try:
            inventario = Inventario.objects.get(sku=sku)
            inventario.tot_unidades += unidades
        except Inventario.DoesNotExist:
            inventario = Inventario(sku=sku, tot_unidades=unidades)
        inventario.save()

    # Recorrer los objetos de Salida
    for salida in Salida.objects.all():
        sku = salida.sku_out
        unidades = salida.unidades_out
        try:
            inventario = Inventario.objects.get(sku=sku)
            inventario.tot_unidades -= unidades
        except Inventario.DoesNotExist:
            inventario = Inventario(sku=sku, tot_unidades=-unidades)
        inventario.save()

'''
recepcion_set es una referencia a la relación inversa de la clase Maestra con la clase Recepcion. En Django, cuando se define una clave foránea en una clase, se crea automáticamente una relación inversa en la clase relacionada.
En este caso, como la clase Recepcion tiene una clave foránea a Maestra, se creó automáticamente un atributo en Maestra llamado recepcion_set que puede ser utilizado para acceder a todas las instancias de Recepcion que tienen una clave foránea a esa instancia de Maestra.
Por ejemplo, si tienes una instancia maestra de Maestra, puedes acceder a todas las instancias de Recepcion que tienen una clave foránea a esa instancia utilizando el atributo maestra.recepcion_set.all().

NECESITO:
- agregar fechas -datafield
- verificador de orden repetida
- gráficos de analisis de datos
- filtro en tablas - agregar un buscador de ordenes 
- agregar en models Class Categoria: para la construccion de las categorias
- como hacer para que los datos se guarden en un formato lower o upper y que los muestre tipo tittle...la busqueda debe transformar en el formato en que esta guardando el dato!
- 

'''