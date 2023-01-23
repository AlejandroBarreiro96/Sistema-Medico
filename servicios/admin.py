from django.contrib import admin
from  .models import Servicio

# Register your models here.

class servicioadmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Servicio, servicioadmin) 