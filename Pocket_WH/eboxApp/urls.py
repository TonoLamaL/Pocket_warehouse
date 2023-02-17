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
    
]
