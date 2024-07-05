from django.db import models

# Create your models here.
class TipoUsuario(models.Model):
    id_tipoUsuario = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion
