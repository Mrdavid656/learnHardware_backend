from django.db import models


class Nivel(models.Model):
    nombre = models.PositiveSmallIntegerField()
    limite_puntos = models.DecimalField(max_digits=5, decimal_places=1)
