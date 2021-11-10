from django.contrib.auth.models import AbstractUser
from django.db import models

from usuarios.models import Nivel


class UserProfile(AbstractUser):
    NOVATO_DIFICULTAD = 0
    SABIONDO_DIFICULTAD = 1
    EXPERTO_DIFICULTDAD = 2
    DIFICULTAD_TYPES_CHOICES = (
        (NOVATO_DIFICULTAD, 'novato'),
        (SABIONDO_DIFICULTAD, 'sabiondo'),
        (EXPERTO_DIFICULTDAD, 'estrella'),
    )

    puntos = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Foreign keys
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, related_name='userprofile_nivel')
    categoria = models.PositiveSmallIntegerField(choices=DIFICULTAD_TYPES_CHOICES, default=NOVATO_DIFICULTAD)


