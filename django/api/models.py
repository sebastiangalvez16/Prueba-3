from django.db import models

class Cliente(models.Model):  # Con mayúscula inicial
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    cliente_id = models.IntegerField()
    edad = models.PositiveSmallIntegerField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    saldo = models.FloatField()
    active = models.BooleanField()
    nivel_de_satisfaccion = models.FloatField()

    def __str__(self):
        return f"Cliente ID: {self.cliente_id}"
