import pytest

from contacto.views import contacto 

def test_user_creation():
	user = contacto.objects.create_user(
	nombre = 'Roque',
	apellido = 'Campoverde',
	cedula = '0912873465',
	email = 'rcam1@gmail.com',
	genero = 'Masculino',
	especialidad = 'General'
	)
	assert user.nombre == 'Roque'