from django.shortcuts import render, HttpResponse

def home(request, template = "SistemaWeb/home.html"):
     return render(request, template, {} )

def servicio(request, template="SistemaWeb/servicios.html"):
     return render(request, template, {})

def tienda(request, template="SistemaWeb/tienda.html"):
     return render(request,template,{} )

def blog(request, template ="SistemaWeb/blog.html"):
     return render(request, template, {})

def contacto(request, tempalte="SistemaWeb/contacto.html"):
     return render(request,tempalte,{} )

def Login(request, tempalte="SistemaWeb/Login.html"):
     return render(request,tempalte,{} )