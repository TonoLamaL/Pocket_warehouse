from django.urls import path
from eboxApp import views

urlpatterns = [
    path('', views.index, name = 'Index'),
    path('maestra/', views.maestra, name = 'Maestra')
]
