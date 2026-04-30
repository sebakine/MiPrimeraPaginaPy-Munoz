from django import forms
from .modelos import Producto, Categoria, Proveedor

class CategoriaFormulario(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class ProveedorFormulario(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'telefono']

class ProductoFormulario(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio']
