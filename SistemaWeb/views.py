from django.shortcuts import render, HttpResponse


def home(request):
     return render(request,"SistemaWeb/home.html" )

def servicio(request):
     return render(request,"SistemaWeb/especialidades.html" )

   

