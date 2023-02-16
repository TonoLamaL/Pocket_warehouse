from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from eboxApp.models import *
from eboxApp.forms import *

def index(request):
    return render (request, 'eboxApp/index.html')

def maestra(request):
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
    if request.method == 'GET': # si existe un post
        busqueda = request.GET['nombre_producto']
        producto = Maestra.objects.filter(nombre_producto = busqueda)
        
        return render(request, 'eboxApp/wMaestra_list.html', {'producto':producto , 'busqueda':busqueda })
    
def buscarMaestra(request):
    if request.method == 'GET': # si existe un post
        producto = Maestra.objects.all()
        
        return render(request, 'eboxApp/wMaestra_full.html', {'producto':producto })