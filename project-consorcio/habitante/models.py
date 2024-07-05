from django.db import models
from inmueble.models import Inmueble

class Habitante(models.Model):
    id_habitante = models.AutoField(primary_key=True)
    id_inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    dni = models.CharField(max_length=20)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

