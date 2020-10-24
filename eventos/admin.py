from django.contrib import admin
from .models import Evento, Usergeneral
# Register your models here.


class Eventoadmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'lugar', 'fecha']
    search_fields = ['id', 'nombre', 'fecha']
    list_filter = ['nombre']


class Generaladmin(admin.ModelAdmin):
    list_display = ['cedula', 'nombre', 'apellido', 'email']
    search_fields = ['cedula', 'nombre', 'apellido', 'email']
    list_filter = ['cedula']


admin.site.register(Evento, Eventoadmin)
admin.site.register(Usergeneral, Generaladmin)
