from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre", required=True) 
    apellido=forms.CharField(label="Apellido", required=True)
    cedula=forms.CharField(label="Cedula", required=True)
    correo=forms.CharField(label="E-mail", required=True)
    genero=forms.CharField(label="Genero", required=True)
    citamedica=forms.CharField(label="Especialidad", required=True)


