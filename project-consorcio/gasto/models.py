from django.db import models

class Gasto(models.Model):
    id_gasto = models.AutoField(primary_key=True)
    descripcion_gasto = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion_gasto
