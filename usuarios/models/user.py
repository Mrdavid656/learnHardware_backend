from django.contrib.auth.models import AbstractUser
from django.db import models

from usuarios.models import Nivel


class UserProfile(AbstractUser):
    puntos = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Foreign keys
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, related_name='userprofile_nivel')


