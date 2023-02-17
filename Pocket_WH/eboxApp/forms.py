from django import forms
from eboxApp.models import *

class MaestraForm(forms.Form):
    nombre_producto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=300)
    numero_sku = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),max_value=99999999999)
    categoria = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=300)
    
class RecepcionForm(forms.Form):
    num_contenedor = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='N° Contenedor',max_length=100)
    sku_in = forms.ModelChoiceField(queryset=Maestra.objects.all(),label='Sku *', widget=forms.Select(attrs={'class': 'form-control'})) #sku_in = forms.ModelChoiceField(queryset=Maestra.objects.filter( numero_sku__gt = 0),label='Sku', widget=forms.Select(attrs={'class': 'form-control'}))
    unidades_in = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),label='Unidades a Ingresar',max_value=99999999999)
    

class EgresoForm(forms.Form):
    orden_venta = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='N° Orden de venta',max_length=100)
    sku_out = forms.ModelChoiceField(queryset=Maestra.objects.all(),label='Sku *', widget=forms.Select(attrs={'class': 'form-control'})) 
    unidades_out = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),label='Unidades vendidas',max_value=99999999999)
    