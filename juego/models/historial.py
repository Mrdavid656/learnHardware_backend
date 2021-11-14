from django.db import models

from juego.models import Trivia
from usuarios.models import UserProfile


class Historial(models.Model):
    usuario = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='Historial_usuario')
    trivia = models.ForeignKey(
        Trivia, on_delete=models.CASCADE, related_name='Historial_trivia')
    puntos = models.DecimalField(max_digits=4, decimal_places=1)
    like = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
