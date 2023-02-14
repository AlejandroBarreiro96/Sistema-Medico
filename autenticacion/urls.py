from django.urls import path

from .views import registro
urlpatterns = [
 
   
    path('',registro.as_view(), name="Autenticacion"),
  
]

