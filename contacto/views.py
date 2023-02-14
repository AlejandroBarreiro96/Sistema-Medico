from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request, templates="contacto/contacto.html"):
     formulario_contact=FormularioContacto()
     if request.method=="POST":
          formulario_contact=FormularioContacto(data=request.POST)
          if formulario_contact.is_valid():
               nombre=request.POST.get("nombre")
               apellido=request.POST.get("apellido")
               cedula=request.POST.get("cedula")
               email=request.POST.get("email")
               genero=request.POST.get("genero")
               especialidad=request.POST.get("citamedica")
               
               email=EmailMessage("mensaje enviado desde el Sitema medico",
               "El paciente con nombre {} apellido {} numero de cedula {} correo electronico {} genero {} requiere una cita medica en la especialidad de:\n\n {}".format(nombre, apellido, cedula, email, genero, especialidad),
               "",["kevalejba@gmail.com"],reply_to=[email])

               try:
                    email.send()
                                                     
                    return redirect("/contacto/?valido")
               except:  
                    return redirect("/contacto/?novalido")
     
     return render(request,templates,{'formulario':formulario_contact} )