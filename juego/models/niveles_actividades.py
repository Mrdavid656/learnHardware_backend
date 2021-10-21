from django.db import models

from juego.models import Leccion


class NivelesActividades(models.Model):
    PRINCIPIANTE_DIFICULTAD = 0
    EXPERIMENTADO_DIFICULTAD = 1
    PROFESIONAL_DIFICULTAD = 2
    DIFICULTAD_TYPES_CHOICES = (
        (PRINCIPIANTE_DIFICULTAD, 'principiante'),
        (EXPERIMENTADO_DIFICULTAD, 'experimentado'),
        (PROFESIONAL_DIFICULTAD, 'profesional'),
    )

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    dificultad = models.PositiveSmallIntegerField(choices=DIFICULTAD_TYPES_CHOICES, default=PRINCIPIANTE_DIFICULTAD)

    # Foreign Key
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE, related_name='NivelesActividades_leccion')
