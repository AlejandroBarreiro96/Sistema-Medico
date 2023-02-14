from django.shortcuts import render, HttpResponse


def servicio(request, template="SistemaWeb/especialidades.html"):
     return render(request, template, {})
def home(request):
     return render(request,"SistemaWeb/home.html" )

def servicio(request):
     return render(request,"SistemaWeb/servicios.html" )

def blog(request):
     return render(request,"SistemaWeb/blog.html" )     

def login(request):
     return render(request,"SistemaWeb/login.html" )


