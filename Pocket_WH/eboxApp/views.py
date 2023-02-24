from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from eboxApp.models import *
from eboxApp.forms import *
from django.contrib import messages
from datetime import date, datetime
# para crear el login lo siguiente
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


def index(request):
    ''' Página de inicio '''
    return render (request, 'eboxApp/index.html')


# MAESTRA 

def maestra(request):
    ''' Formulario para crear nuevos productos en la maestra de productos - te llevo a una ventana distinta con boton volver'''
    success = True
    if request.method == 'POST': # si existe un post
        maestra_prod = MaestraForm(data=request.POST)
        print (maestra_prod)
        
        # una validacion que pide django ({% csrf_token %}) en el html
        if maestra_prod.is_valid():
            informacion = maestra_prod.cleaned_data
            nuevo_producto = Maestra(nombre_producto = informacion['nombre_producto'], numero_sku = informacion['numero_sku'], categoria = informacion['categoria']) # son los argumentos de la clase y la guardo en el objeto     
            nuevo_producto.save()
            success = True
            maestra_prod = MaestraForm()
            return render(request, 'eboxApp/maestra.html', {'maestra_prod':maestra_prod, 'success': success}) # le entrego el conexto de success para me muestre el mensaje que le digo en el html
            #return render(request, 'eboxApp/windowsConfirm.html') # una vez que se guardo que retorne a la pagina de confrimación, y desde la confirmacion window hice un html que me retorna a inicio
    else:
        maestra_prod = MaestraForm()
        success = False
    
    return render(request, 'eboxApp/maestra.html', {'maestra_prod':maestra_prod, 'success': success})


def buscarProducto(request):
    ''' Formulario para buscar un producto en especifico por su nombre - te llevo a una ventana distinta con boton volver'''
    if request.method == 'GET': # si existe un get
        busqueda = request.GET['nombre_producto']
        #busqueda = busqueda.lower()
        producto = Maestra.objects.filter(nombre_producto = busqueda)
        
        return render(request, 'eboxApp/wMaestra_list.html', {'producto':producto , 'busqueda':busqueda })
    
def buscarMaestra(request):
    '''funcion para traer todos los elementos creados en el formulario de maestra'''
    ''' Boton de busqueda completa de la maestra con respuesta en una lista - te llevo a una ventana distinta con boton volver'''
    if request.method == 'GET': # si existe un get
        producto = Maestra.objects.all() # busco todo lo que hay en la maestra
        
        return render(request, 'eboxApp/wMaestra_full.html', {'producto':producto }) # aqui le digo donde quiero mostrar "producto"

def eliminarProducto(request, numero_sku):
    '''función para eliminar un prodiucto que ya no quiero tener'''
    producto = Maestra.objects.get(numero_sku=numero_sku )
    producto.delete()

    producto = Maestra.objects.all() # debo usar el mismo nombre que cuando renderizo la busqueda completa de la maestra en buscarMaestra
    return redirect('eboxApp:buscarTodo')

'''debi poner un filtro para que no elimine de la maestra mercaderia que tinee movimientos, mejor hacer editar'''

def editarProducto(request, numero_sku): # la idea es que te llebe devuelta ala paigna de creacion en maestra pero no los datos y modificarlos
    '''función para editar un producto del catálogo'''
    producto = Maestra.objects.get(numero_sku=numero_sku )
    if request.method == 'POST':
        maestra_prod = MaestraForm(request.POST)
        print(maestra_prod)
        
        if maestra_prod.is_valid():
            informacion = maestra_prod.cleaned_data
            
            producto.nombre_producto = informacion['nombre_producto']
            producto.numero_sku = informacion['numero_sku']
            producto.categoria = informacion['categoria']

            producto.save()            
            return redirect('eboxApp:buscarTodo')
    else:
        
        maestra_prod = MaestraForm(initial={'nombre_producto': producto.nombre_producto, 'numero_sku':producto.numero_sku,'categoria':producto.categoria })
    
    return render (request,'eboxApp/editarProducto.html', {'maestra_prod':maestra_prod, 'numero_sku':numero_sku } )


# RECEPCIÓN
def recepcion(request):
    " Formulario para crear una recepción que tiene que ingresar productos al inventario"
    success = False
    if request.method == 'POST': # si existe un post
        recepcion_prod = RecepcionForm(data=request.POST)
        print (recepcion_prod)
        
        # una validacion que pide django ({% csrf_token %})
        if recepcion_prod.is_valid():
            informacion = recepcion_prod.cleaned_data
            nueva_recepcion = Recepcion(num_contenedor = informacion['num_contenedor'], sku_in = informacion['sku_in'], unidades_in = informacion['unidades_in'],fecha_recepcion=date.today(), orden_compra = informacion['orden_compra']) # asignar la fecha actual) # son los argumentos de la clase y la guardo en el objeto     
            nueva_recepcion.save()
            success = True
            recepcion_prod = RecepcionForm()
            return render(request, 'eboxApp/recepcion.html', {'recepcion_prod':recepcion_prod, 'success': success}) # si funciona que renderizo esto. le entrego el conexto de success para me muestre el mensaje que le digo en el html
            #return render(request, 'eboxApp/windowsConfirm.html') # una vez que se guardo que retorne a la pagina de confrimación, y desde la confirmacion window hice un html que me retorna a inicio

            

    else:
        recepcion_prod = RecepcionForm()
        success = False
    
    return render(request, 'eboxApp/recepcion.html', {'recepcion_prod':recepcion_prod})

def buscarRecepcion(request):
    ''' Boton de busqueda completa de las recepciones con respuesta en una lista - te llevo a una ventana distinta con boton volver'''
    if request.method == 'GET': # si existe una solicitud, get 
        recepciones = Recepcion.objects.all()
        
        return render(request, 'eboxApp/wRecepcion_full.html', {'recepciones':recepciones })

# CREACIÓN DE ORDENES
def egreso(request):
    " Formulario para crear un egreso que tiene que salir productos al inventario"
    success = False
    if request.method == "POST":
        form = EgresoForm(data=request.POST)
        print (form)
    
        if form.is_valid():
            sku_out = form.cleaned_data["sku_out"]
            unidades_out = form.cleaned_data["unidades_out"]
            orden_venta = form.cleaned_data["orden_venta"]
            fecha_despacho = form.cleaned_data["fecha_despacho"]
            
            fecha_str = fecha_despacho.strftime('%d-%m-%Y') # tranformo la fecha en el formato string 
            fecha_despacho = datetime.strptime(fecha_str, '%d-%m-%Y').date() # uso la fecha de despacho con formato fecha 

            
            try:
                inventario = Inventario.objects.get(sku=sku_out) # intenta buscar el sku de inventario = sku_out de egreso puesto en el formulario.
                
                if inventario.tot_unidades - unidades_out < 0: # accedo a la variable inventario
                    messages.error(request, "No puedes preparar ese pedido. Las unidades que pides no alcanzan, ajusta las unidades.")
                    print(messages)
                    return render(request, "eboxApp/egreso.html", {"form": form})
                else:
                    Salida.objects.create(sku_out=sku_out, unidades_out=unidades_out, orden_venta=orden_venta, fecha_despacho=fecha_despacho)
                    inventario.tot_unidades -= unidades_out
                    inventario.save()
                    success = True
                    form = EgresoForm()
                    return render(request, 'eboxApp/egreso.html', {'form':form, 'success': success}) # le entrego el conexto de success para me muestre el mensaje que le digo en el html
                    
                    #return render(request, 'eboxApp/windowsConfirm.html') # una vez que se guardo que retorne a la pagina de confrimación, y desde la confirmacion window hice un html que me retorna a inicio
            except ObjectDoesNotExist:
                Inventario.objects.create(sku=sku_out, tot_unidades=unidades_out)
                Salida.objects.create(sku_out=sku_out, unidades_out=unidades_out, orden_venta=orden_venta,fecha_despacho=fecha_despacho)
                return render(request, 'eboxApp/windowsConfirm.html') # creo que esto no aplica porque no puedo crear egresos de prooductos que no existen en la maestra, y me estan quedando ahi cuando estan en cero. Si los elimino cuando llegan a 0 podría ser util
    else:
        form = EgresoForm()
        success = False

    return render(request, "eboxApp/egreso.html", {"form": form})
'''
PARA QUE ES EL CONTEXTO EN UN RENDER:

El contexto es un diccionario de Python que se utiliza para pasar datos a una plantilla HTML en Django. 
Básicamente, permite que la vista de Django envíe información a la plantilla HTML para que esta última pueda mostrar la información de manera dinámica.
El diccionario de contexto se pasa como argumento a la función render(), que se utiliza para generar una respuesta HTTP que contiene la plantilla HTML.
Los elementos del diccionario se pueden acceder en la plantilla HTML utilizando el sistema de plantillas de Django, que utiliza etiquetas como {{}} o {% %}.

'''

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
 
 #REGISTRO, LOGIN y LOGOUT -> hay que asignar funciones
 
 # funciones de django hace automaticamente el trabajo!
def login_request(request):
        if request.method == 'POST':
            form_login = CustomUserLoginForm(data = request.POST)

            if form_login.is_valid():
                usuario = form_login.cleaned_data.get('username') # el () es del get, debe coicidir con la variable en form
                contraseña = form_login.cleaned_data.get('password') # debe coicidir con la variable en form
                
                user = authenticate(request, username = usuario, password = contraseña)
                
                if user is not None: #si usuario no esta vacío (osea si estas logeado)
                    login(request,user)
                    return render(request, "eboxApp/index.html", {'Mensaje': f'Bienvenido {usuario}'})
                else:
                    form_login = CustomUserLoginForm()
                    return render(request, "eboxApp/login.html", {'Mensaje': f'Credenciales invalidas', 'form_login': form_login})

            else:
                form_login = CustomUserLoginForm()
                return render(request, "eboxApp/login.html", {'Mensaje': f'Credenciales invalidas', 'form_login': form_login})
            
        form_login = CustomUserLoginForm()
        return render (request, "eboxApp/login.html", {'form_login' : form_login})
    
#funciones de django hace automaticamente el trabajo! 
           
def register_request(request):
    if request.method == 'POST':
        form_register = UserRegisterForm(request.POST)
        
        if form_register.is_valid():
            form_register.save()
            return render(request, "eboxApp/index.html", {'Mensaje': 'Usuario creado'})
    else:
        form_register = UserRegisterForm()
    
    return render(request, "eboxApp/registro.html", {'form_register': form_register})

def logout_request(request):
    logout(request)
    return render (request, "eboxApp/index.html")

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
- agregar fechas -datafield -> OK (costo mas que la mierda)
- verificador de orden repetida
- gráficos de analisis de datos
- filtro en tablas - agregar un buscador de ordenes 
- agregar en models Class Categoria: para la construccion de las categorias
- como hacer para que los datos se guarden en un formato lower o upper y que los muestre tipo tittle...la busqueda debe transformar en el formato en que esta guardando el dato!
- 

'''