from django.db import models
from habitante.models import Habitante  # Asegúrate de tener el modelo Habitante creado
from inmueble.models import Inmueble  # Asegúrate de tener el modelo Inmueble creado

class Cabecera(models.Model):
    id_cabecera = models.AutoField(primary_key=True)
    id_habitante = models.ForeignKey(Habitante, on_delete=models.CASCADE)
    id_inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    fecha = models.DateField()
    total_gastos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Informe {self.id_cabecera} - Cliente: {self.cliente.nombre}'

    def calcular_total(self):
        """Calcula y actualiza el total de los gastos en la cabecera"""
        total = sum(detalle.importe for detalle in self.detalles.all())
        self.total_gastos = total
        self.save()
        return total