from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from eboxApp.models import *
from eboxApp.forms import *

def index(request):
    ''' Página de inicio '''
    return render (request, 'eboxApp/index.html')


# MAESTRA 
def maestra(request):
    ''' Formulario para crear nuevos productos en la maestra de productos - te llevo a una ventana distinta con boton volver'''
    if request.method == 'POST': # si existe un post
        maestra_prod = MaestraForm(data=request.POST)
        print (maestra_prod)
        
        # una validacion que pide django ({% csrf_token %})
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
    if request.method == 'POST': # si existe un post
        egreso_prod = EgresoForm(data=request.POST)
        print (egreso_prod)
        
        # una validacion que pide django ({% csrf_token %})
        if egreso_prod.is_valid():
            informacion = egreso_prod.cleaned_data
            nueva_salida = Salida(orden_venta = informacion['orden_venta'], sku_out = informacion['sku_out'], unidades_out = informacion['unidades_out']) # son los argumentos de la clase y la guardo en el objeto     
            nueva_salida.save()
            return render(request, 'eboxApp/windowsConfirm.html') # una vez que se guardo que retorne a la pagina de confrimación, y desde la confirmacion window hice un html que me retorna a inicio

    else:
        egreso_prod = EgresoForm()
    
    return render(request, 'eboxApp/egreso.html', {'egreso_prod':egreso_prod})

def buscarEgreso(request):
    ''' Boton de busqueda completa de las ordenes de compra con respuesta en una lista - te llevo a una ventana distinta con boton volver'''
    if request.method == 'GET': # si existe un post
        salidas = Salida.objects.all()
        
        return render(request, 'eboxApp/wEgreso_full.html', {'salidas':salidas })



# KARDEX 

