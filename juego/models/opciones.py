from django.db import models

from juego.models import Trivia


class Opciones(models.Model):
    opcion = models.CharField(max_length=200)
    opcion_correcta = models.BooleanField(default=False)

    # Foreign Key
    trivia = models.ForeignKey(Trivia, on_delete=models.CASCADE, related_name='Opciones_trivia')
