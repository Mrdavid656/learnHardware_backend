from django.db import models


class Nivel(models.Model):
    nombre = models.PositiveSmallIntegerField(unique=True)
    limite_puntos = models.DecimalField(max_digits=5, decimal_places=1)
