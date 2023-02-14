from django.shortcuts import render, HttpResponse


def home(request):
     return render(request,"SistemaWeb/home.html" )

def servicio(request):
     return render(request,"SistemaWeb/especialidades.html" )

def blog(request):
     return render(request,"SistemaWeb/blog.html" )     

def login(request):
     return render(request,"SistemaWeb/login.html" )


