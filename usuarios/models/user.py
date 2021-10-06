from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    puntos = models.DecimalField(max_digits=10, decimal_places=2)

    # Foreign keys
    nivel = models.IntegerField()
