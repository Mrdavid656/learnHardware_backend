from django.db import models


class Leccion(models.Model):
    NOVATO_DIFICULTAD = 0
    SABIONDO_DIFICULTAD = 1
    EXPERTO_DIFICULTDAD = 2
    DIFICULTAD_TYPES_CHOICES = (
        (NOVATO_DIFICULTAD, 'novato'),
        (SABIONDO_DIFICULTAD, 'sabiondo'),
        (EXPERTO_DIFICULTDAD, 'estrella'),
    )

    titulo = models.CharField(max_length=200)
    resumen = models.CharField(max_length=200)
    informacion = models.TextField()
    keywords = models.CharField(max_length=100)
    categoria = models.PositiveSmallIntegerField(choices=DIFICULTAD_TYPES_CHOICES, default=NOVATO_DIFICULTAD)
