from django.db import models

# Create your models here.
class TipoPago(models.Model):
    id_tipo_pago = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length = 255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"IngresoDetalle {self.id_tipo_pago} - tipo: {self.tipo}"