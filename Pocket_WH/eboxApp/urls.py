from django.urls import path
from eboxApp import views

urlpatterns = [
    path('', views.index, name = 'index'),
]
