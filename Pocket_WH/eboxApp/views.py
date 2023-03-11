from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from eboxApp.models import *
from eboxApp.forms import *
from django.contrib import messages
from datetime import date, datetime
# para crear el login lo siguiente
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required



def index(request):
    ''' Página de inicio '''
    return render (request, 'eboxApp/index.html')


# MAESTRA 
@login_required
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

@login_required
def buscarProducto(request):
    ''' Formulario para buscar un producto en especifico por su nombre - te llevo a una ventana distinta con boton volver'''
    if request.method == 'GET': # si existe un get
        busqueda = request.GET['nombre_producto']
        #busqueda = busqueda.lower()
        producto = Maestra.objects.filter(nombre_producto = busqueda)
        
        return render(request, 'eboxApp/wMaestra_list.html', {'producto':producto , 'busqueda':busqueda })
@login_required    
def buscarMaestra(request):
    '''funcion para traer todos los elementos creados en el formulario de maestra'''
    ''' Boton de busqueda completa de la maestra con respuesta en una lista - te llevo a una ventana distinta con boton volver'''
    if request.method == 'GET': # si existe un get
        producto = Maestra.objects.all() # busco todo lo que hay en la maestra
        
        return render(request, 'eboxApp/wMaestra_full.html', {'producto':producto }) # aqui le digo donde quiero mostrar "producto"
@login_required
def eliminarProducto(request, numero_sku):
    '''función para eliminar un prodiucto que ya no quiero tener'''
    producto = Maestra.objects.get(numero_sku=numero_sku )
    producto.delete()

    producto = Maestra.objects.all() # debo usar el mismo nombre que cuando renderizo la busqueda completa de la maestra en buscarMaestra
    return redirect('eboxApp:buscarTodo')

'''debi poner un filtro para que no elimine de la maestra mercaderia que tinee movimientos, mejor hacer editar'''
@login_required
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
@login_required
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

@login_required
def buscarRecepcion(request):
    ''' Boton de busqueda completa de las recepciones con respuesta en una lista - te llevo a una ventana distinta con boton volver'''
    if request.method == 'GET': # si existe una solicitud, get 
        recepciones = Recepcion.objects.all()
        
        return render(request, 'eboxApp/wRecepcion_full.html', {'recepciones':recepciones })

# CREACIÓN DE ORDENES
@login_required
def egreso(request):
    " Formulario para crear un egreso que tiene que salir productos al inventario"
    success = False
    if request.method == "POST":
        form = EgresoForm(data=request.POST)
        if form.is_valid():
            sku_out = form.cleaned_data["sku_out"]
            unidades_out = form.cleaned_data["unidades_out"]
            orden_venta = form.cleaned_data["orden_venta"]
            fecha_despacho = form.cleaned_data["fecha_despacho"]
            
            fecha_str = fecha_despacho.strftime('%d-%m-%Y') # tranformo la fecha en el formato string 
            fecha_despacho = datetime.strptime(fecha_str, '%d-%m-%Y').date() # uso la fecha de despacho con formato fecha 

            try:
                inventario = Inventario.objects.get(sku=sku_out) # intenta buscar el sku de inventario = sku_out de egreso puesto en el formulario.
                
                if inventario.unidades_disponibles - unidades_out < 0: # accedo a la variable inventario
                    messages.error(request, "No puedes preparar ese pedido. Las unidades que pides no alcanzan, ajusta las unidades.")
                    print(messages)
                    return render(request, "eboxApp/egreso.html", {"form": form})
                else:
                    # Actualiza las unidades disponibles y las unidades reservadas
                    inventario.unidades_reservadas += unidades_out
                    inventario.unidades_disponibles = inventario.tot_unidades - inventario.unidades_reservadas
                    inventario.save()

                    Salida.objects.create(sku_out=sku_out, unidades_out=unidades_out, orden_venta=orden_venta, fecha_despacho=fecha_despacho, estado=Estados.objects.get(pk=1)) # predeterminado en estado pendiente
                    
                    success = True
                    form = EgresoForm()
                    return render(request, 'eboxApp/egreso.html', {'form':form, 'success': success})
                    
            except ObjectDoesNotExist:
                messages.error(request, "Aún no haz recibido unidades de este producto. No puedes preparar ese pedido.")
                return render(request, "eboxApp/egreso.html", {"form": form})
    else:
        form = EgresoForm()
        success = False

    return render(request, "eboxApp/egreso.html", {"form": form})




@login_required
def despachos_pendientes(request):
    # Obtener la fecha actual para compararla con la fecha de despacho de los pedidos
    fecha_actual = date.today()

    # Obtener todos los pedidos pendientes de despacho cuya fecha de despacho sea posterior o igual a la fecha actual
    pedidos_pendientes = Salida.objects.filter(fecha_despacho__gte=fecha_actual)

    return render(request, "eboxApp/despachos_pendientes.html", {"pedidos_pendientes": pedidos_pendientes})

'''
PARA QUE ES EL CONTEXTO EN UN RENDER:

El contexto es un diccionario de Python que se utiliza para pasar datos a una plantilla HTML en Django. 
Básicamente, permite que la vista de Django envíe información a la plantilla HTML para que esta última pueda mostrar la información de manera dinámica.
El diccionario de contexto se pasa como argumento a la función render(), que se utiliza para generar una respuesta HTTP que contiene la plantilla HTML.
Los elementos del diccionario se pueden acceder en la plantilla HTML utilizando el sistema de plantillas de Django, que utiliza etiquetas como {{}} o {% %}.

'''
@login_required
def buscarEgreso(request):
    ''' Boton de busqueda completa de las ordenes de compra con respuesta en una lista - te llevo a una ventana distinta con boton volver'''
    if request.method == 'GET':
        form = SelectEstados()
        salidas = Salida.objects.all()
        
        return render(request, 'eboxApp/wEgreso_full.html', {'salidas':salidas, 'form': form})
    elif request.method == 'POST':
        form = SelectEstados(request.POST)
        salidas = Salida.objects.all()
        if form.is_valid():
            estado = form.cleaned_data['estado']
            seleccionados = request.POST.getlist('seleccionados')
            Salida.objects.filter(pk__in=seleccionados).update(estado=estado)
            return redirect('eboxApp:buscarTodoEgreso')
        
        return render(request, 'eboxApp/wEgreso_full.html', {'salidas':salidas, 'form': form})




@login_required
def actualizarEstado(request, id_salida):
    '''funcion para cambiar de estado. cuando esta en pendiente quita unidades disponibles y agrega en reservado
    si esta en cancelado retorna unidades a reservado, si esta preparado quita unidades disponible y agrega a rpeparado, si esta en entregado quita en disponible
    y en reservado. solo se puede pasar a entregado desde estado anterior preparado'''
    salida = Salida.objects.get(pk=id_salida)

    if request.method == 'POST':
        form = SelectEstados(request.POST)
        if form.is_valid():
            nuevo_estado = form.cleaned_data['estado']
            unidades = salida.unidades_out  # obtener las unidades de la salida
            inventario = Inventario.objects.get(sku=salida.sku_out)

            if nuevo_estado.pk == 3 and salida.estado.pk != 2: # si el estado es "entregado" y la salida no está en estado "Preparado"
                messages.warning(request, 'No se puede actualizar el estado de una salida entregada que NO esté en estado "Preparado".')
            else:
                if nuevo_estado.pk not in [1, 4, 3]:  # si el estado no es 'Pendiente' o "cancelado" o "entregado"
                    inventario.unidades_reservadas -= unidades
                    inventario.unidades_preparadas += unidades
                    inventario.tot_unidades -= unidades # actualizar el inventario
                    inventario.save()
                elif nuevo_estado.pk == 4: # si el estado es "cancelado"
                    inventario.unidades_reservadas += unidades
                    inventario.unidades_preparadas -= unidades
                    inventario.tot_unidades += unidades # actualizar el inventario
                    inventario.save()
                elif nuevo_estado.pk == 3:# si el estado es "entregado"
                    inventario.unidades_entregadas += unidades
                    inventario.unidades_preparadas -= unidades
                    inventario.save()

                salida.estado_anterior = salida.estado  # almacenar el estado anterior en el campo estado_anterior
                salida.estado = nuevo_estado
                salida.save()
                return redirect('eboxApp:buscarTodoEgreso')
    else:
        form = SelectEstados(initial={'estado': salida.estado})

    return render(request, 'eboxApp/actualizar_estado.html', {'form': form, 'salida': salida})






# INVENTARIO

@login_required
def stock_en_linea(request):
    '''funcion para revisar el stock en linea - esta es solo para mostrar - las funciones son
    parte de las clases Recepcion y Salida '''
    inventarios = Inventario.objects.all()
    return render(request, 'eboxApp/stock_en_linea.html', {'inventarios': inventarios})
 
 #REGISTRO, LOGIN y LOGOUT -> hay que asignar funciones
 

def login_request(request):
        '''función de inicio de sesion'''
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
    """función de registro"""
    if request.method == 'POST':
        form_register = UserRegisterForm(request.POST)
        
        if form_register.is_valid():
            form_register.save()
            return render(request, "eboxApp/index.html", {'Mensaje': 'Usuario creado'})
    else:
        form_register = UserRegisterForm()
    
    return render(request, "eboxApp/registro.html", {'form_register': form_register})

def logout_request(request):
    """función logout"""
    logout(request)
    return render (request, "eboxApp/index.html")

def about(request):
    """pagina quienes somos"""
    return render (request,"eboxApp/about.html")

def terms(request):
    """termino y condiciones"""
    return render (request,"eboxApp/terms.html")

 # FUNCIONES DE USO INTENRO AQUI ABAJO llamdas desde la terminal
 
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