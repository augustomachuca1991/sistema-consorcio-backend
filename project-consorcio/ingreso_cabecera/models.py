from django.db import models

# Create your models here.
class IngresoCabecera(models.Model):
    id_ingreso_cabecera = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return f"IngresoCabecera {self.id_ingreso_cabecera} - Total: {self.total}"
