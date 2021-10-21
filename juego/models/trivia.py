from django.db import models

from juego.models import NivelesActividades


class Trivia(models.Model):
    pregunta = models.CharField(max_length=300)

    # Foreign Key
    actividad = models.ForeignKey(NivelesActividades, on_delete=models.CASCADE, related_name='Trivia_actividades')
