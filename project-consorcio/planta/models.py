from django.db import models

class Planta(models.Model):
    id_planta = models.AutoField(primary_key=True)
    descripcion_planta = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion_planta
