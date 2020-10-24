from django.db import models

# Create your models here.


class Evento(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=100)
    lugar = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.CharField(max_length=10)
    boletos = models.CharField(max_length=5)
    precio = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre


class Usergeneral(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    boletos = models.CharField(max_length=5)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
