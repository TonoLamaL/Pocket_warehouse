from django.urls import path
from eboxApp import views


app_name = "eboxApp"
urlpatterns = [
    path('', views.index, name = 'Index'),
    path('maestra/', views.maestra, name = 'Maestra'),
    path('maestra/wMaestra_list/', views.buscarProducto, name = 'buscarProducto'),
    path('maestra/wMaestra_full/', views.buscarMaestra, name = 'buscarTodo'),
    path('recepcion/', views.recepcion, name = 'Recepcion'),
    path('recepcion/wRecepcion_full/', views.buscarRecepcion, name = 'buscarTodoRecepcion'),
    path('egreso/', views.egreso, name = 'Egreso'),
    path('egreso/wEgreso_full/', views.buscarEgreso, name = 'buscarTodoEgreso'),
    path('stock_en_linea/', views.stock_en_linea, name='stock_en_linea'),
    #path('actualizar_inventario/', views.actualizar_inventario, name='Actualizar'),
    path('login', views.login_request,name = 'Login' ),
    path('registro', views.register_request,name = 'Registro' ),
    path('logout/', views.logout_request, name='logout'),
    path('eliminarProducto/<numero_sku>/', views.eliminarProducto, name = 'EliminarProducto'),
    path('editarProducto/<numero_sku>/', views.editarProducto, name = 'EditarProducto'),
    path('about/', views.about, name='about'),
    path('terms/', views.terms, name='Terms'),
    path('despachos_pendientes/', views.despachos_pendientes, name='despachos_pendientes'),
    path('salida/<int:id_salida>/actualizar_estados/', views.actualizarEstado, name='actualizar_estados'),
    path('contacto/', views.contacto, name='contacto'),
    

]
