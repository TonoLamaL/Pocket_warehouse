from django import forms

class MaestraForm(forms.Form):
    nombre_producto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=300)
    numero_sku = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),max_value=99999999999)
    categoria = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=300)