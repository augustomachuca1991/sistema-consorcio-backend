from django.db import models
from tipo_pago.models import TipoPago
from ingreso_cabecera.models import IngresoCabecera



# Create your models here.
class IngresoDetalle(models.Model):
    id_ingreso_detalle = models.AutoField(primary_key=True)
    concepto = models.CharField(max_length = 255)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    saldo = models.DecimalField(max_digits = 10, decimal_places =2)
    created_at = models.DateTimeField(auto_now_add=True)
    id_tipo_pago = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    id_ingreso_cabecera = models.ForeignKey(IngresoCabecera, on_delete=models.CASCADE) 
    importe = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return f"IngresoDetalle {self.id_ingreso_detalle} - concepto: {self.concepto}"