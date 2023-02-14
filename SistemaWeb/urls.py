from django.urls import path

from SistemaWeb import views
urlpatterns = [
 
    path('', views.home, name="Home"),
    path('especialidades', views.servicio, name="Especialidades"),
    path('blog', views.blog, name="Blog"),
    path('contacto', views.contacto, name="Contacto"),
    path('login', views.login, name="Login"),
]
