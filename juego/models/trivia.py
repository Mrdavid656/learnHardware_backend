from django.db import models

from juego.models import Leccion


class Trivia(models.Model):
    PREGUNTAS_TYPE = 0
    IMAGENES_TYPE = 1

    TYPE_CHOICES = (
        (PREGUNTAS_TYPE, 'preguntas'),
        (IMAGENES_TYPE, 'imagenes'),
    )

    pregunta = models.CharField(max_length=300)
    instrucciones = models.CharField(max_length=200)
    tipo = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=PREGUNTAS_TYPE)

    # Foreign Key
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE, related_name='Trivia_leccion')
