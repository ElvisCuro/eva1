from django.db import models

class SensorData(models.Model):
    id = models.IntegerField(primary_key=True)
    valor = models.FloatField()
    voltaje = models.FloatField()
    voltaje_corregido = models.FloatField()

    def __str__(self):
        return f"Valor: {self.valor}, Voltaje: {self.voltaje}, Voltaje corregido: {self.voltaje_corregido}"

