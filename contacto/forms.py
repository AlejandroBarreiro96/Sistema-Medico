from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label="nombre", required=True) 
    apellido=forms.CharField(label="apellido", required=True)
    cedula=forms.CharField(label="cedula", required=True)
    correo=forms.CharField(label="email", required=True)
    genero=forms.CharField(label="genero", required=True)
    citamedica=forms.CharField(label="especialidad", required=True)


