from django import forms
from eboxApp.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, User

class MaestraForm(forms.Form):
    nombre_producto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=300)
    numero_sku = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Es un identificador del producto. Puedes usar letras + números'}),max_length=300)
    categoria = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }),max_length=300)
    
class RecepcionForm(forms.Form):
    num_contenedor = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='N° Contenedor o Nombre del proveedor',max_length=100)
    orden_compra = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='Orden de compra',max_length=100)
    sku_in = forms.ModelChoiceField(queryset=Maestra.objects.all(),label='Sku *', widget=forms.Select(attrs={'class': 'form-control'})) #sku_in = forms.ModelChoiceField(queryset=Maestra.objects.filter( numero_sku__gt = 0),label='Sku', widget=forms.Select(attrs={'class': 'form-control'}))
    unidades_in = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),label='Unidades a Ingresar',max_value=99999999999)
    

class EgresoForm(forms.Form):
    orden_venta = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='N° Orden de venta',max_length=100)
    sku_out = forms.ModelChoiceField(queryset=Maestra.objects.all(),label='Sku *', widget=forms.Select(attrs={'class': 'form-control'})) 
    unidades_out = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),label='Unidades vendidas',max_value=99999999999)
    fecha_despacho = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','placeholder': 'Introduce el formato DD-MM-AAAA','format':'%d-%m-%y'}), input_formats =['%d/%m/%Y', '%d/%m/%y', '%d-%m-%Y', '%d-%m-%y', 'dd/mm/yyyy'],label='Fecha de despacho')
    

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Correo', max_length=100)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Usuario', max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Contraseña', max_length=100)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Confirmar contraseña', max_length=100)
    

    class Meta:
        model = User
        fields = ['username', 'email']
        help_texts = {k: "" for k in fields}

class CustomUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Constraseña'})
        