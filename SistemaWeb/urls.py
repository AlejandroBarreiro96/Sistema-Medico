from django.urls import path

from SistemaWeb import views
urlpatterns = [
 
    path('', views.home, name="Home"),
    path('especialidades', views.servicio, name="Especialidades"),
    
    
    
]
