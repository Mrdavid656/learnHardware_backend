from django.db import models

from juego.models import NivelesActividades


class ReconocimientoImagenes(models.Model):
    pregunta = models.CharField(max_length=200)

    # Foreign keys
    actividad = models.ForeignKey(
        NivelesActividades, on_delete=models.CASCADE, related_name='ReconocimientoImagenes_actividad')
