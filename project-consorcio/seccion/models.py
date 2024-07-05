from django.db import models

# Create your models here.
class Seccion(models.Model):
    id_seccion = models.AutoField(primary_key=True)
    descripcion_seccion = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion_seccion