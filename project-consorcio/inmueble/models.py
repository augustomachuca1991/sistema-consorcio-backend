from django.db import models
from edificio.models import Edificio

class Inmueble(models.Model):
    id_inmueble = models.AutoField(primary_key=True)
    id_edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=255)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inmueble #{self.id_inmueble} - {self.ubicacion}"