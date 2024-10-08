from django.db import models
from gasto.models import Gasto  # Asegúrate de tener el modelo Gasto creado
from cabecera.models import Cabecera

class Detalle(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_cabecera = models.ForeignKey(Cabecera, related_name='detalles', on_delete=models.CASCADE)
    id_gasto = models.ForeignKey(Gasto, on_delete=models.CASCADE)  # Referencia al gasto seleccionado
    importe = models.DecimalField(max_digits=10, decimal_places=2) #esto seria el importe que coresponde al inquilino
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.gasto.descripcion} - Importe: {self.importe}'