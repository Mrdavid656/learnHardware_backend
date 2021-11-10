from django.db import models

from juego.models import Leccion


class RecursoLecciones(models.Model):
    archivo = models.FileField(db_column='image_url', blank=False, null=False, upload_to='images/lecciones')
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE, related_name='RecursosHasLecciones_leccion')
