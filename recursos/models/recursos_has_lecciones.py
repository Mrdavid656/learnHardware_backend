from django.db import models

from juego.models import Leccion
from recursos.models import RecursoLecciones


class RecursosHasLecciones(models.Model):
    recurso_leccion = models.ForeignKey(
        RecursoLecciones,
        on_delete=models.CASCADE,
        related_name='RecursosHasLecciones_recurso_leccion'
    )
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE, related_name='RecursosHasLecciones_leccion')
