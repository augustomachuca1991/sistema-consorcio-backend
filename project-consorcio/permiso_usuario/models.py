from django.db import models

# Create your models here.
class PermisoUsuario(models.Model):
    id_permiso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre