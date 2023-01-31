from django.urls import path

from SistemaWeb import views
urlpatterns = [
 
    path('', views.home, name="Home"),
    path('servicio', views.servicio, name="Servicios"),
    path('tienda', views.tienda, name="Tienda"),
    path('blog', views.blog, name="Blog"),
    path('contacto', views.contacto, name="Contacto"),
    path('Login', views.Login, name="Login"),
]
