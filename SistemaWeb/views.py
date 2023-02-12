from django.shortcuts import render, HttpResponse

def home(request, template = "SistemaWeb/home.html"):
     return render(request, template, {} )

def servicio(request, template="SistemaWeb/servicios.html"):
     return render(request, template, {})

def blog(request, template ="SistemaWeb/blog.html"):
     return render(request, template, {})

def contacto(request, tempalte="SistemaWeb/contacto.html"):
     return render(request,tempalte,{} )

def login(request, template="SistemaWeb/login.html"):
     return render(request,template,{} )
