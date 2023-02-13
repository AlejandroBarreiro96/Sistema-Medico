from django.urls import path

from SistemaWeb import views
urlpatterns = [
 
    path('', views.home, name="Home"),
    path('servicio', views.servicio, name="Servicios"),
    path('blog', views.blog, name="Blog"),
    
    path('login', views.login, name="Login"),
]
