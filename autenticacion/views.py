from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages

# Create your views here.
class registro(View):
    def get(self, request):
        form=UserCreationForm()
        return render(request,"registro/registro.html",{"form":form})

    def post(self, request):
        form=UserCreationForm(request.POST)
        
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect('Home')

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            
            return render(request,"registro/registro.html",{"form":form})


def cerrar_sesion(request):
    logout(request)

    return redirect('Home')
def logonear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_u=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_u, password=clave)
            if usuario is not None:
                login(request,usuario)
                return redirect('Home')
            else:
                messages.error(request, "usuario no existe")
        else:
            messages.error(request, "usuario no valido")

    form=AuthenticationForm()
    return render(request,"login/login.html",{"form":form})
