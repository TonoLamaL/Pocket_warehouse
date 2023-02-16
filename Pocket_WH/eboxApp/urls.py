from django.urls import path
from eboxApp import views

urlpatterns = [
    path('', views.index, name = 'Index'),
    path('maestra/', views.maestra, name = 'Maestra'),
    path('maestra/wMaestra_list/', views.buscarProducto, name = 'buscarProducto'),
    path('maestra/wMaestra_full/', views.buscarMaestra, name = 'buscarTodo'),
]
