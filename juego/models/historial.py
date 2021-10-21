from django.db import models

from juego.models import NivelesActividades
from usuarios.models import UserProfile


class Historial(models.Model):
    usuario = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='Historial_usuario')
    niveles_actividades = models.ForeignKey(
        NivelesActividades, on_delete=models.CASCADE, related_name='Historial_nivelesactividades')
    puntos = models.DecimalField(max_digits=4, decimal_places=1)
    like = models.BooleanField(default=False)
