from django.db import models

from juego.models import Logros
from usuarios.models import UserProfile


class UserLogros(models.Model):
    usuario = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="UserLogros_usuario")
    logro = models.ForeignKey(Logros, on_delete=models.CASCADE, related_name="UserLogros_logro")
