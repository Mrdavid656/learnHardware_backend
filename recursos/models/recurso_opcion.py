from django.db import models

from juego.models import Opciones


class RecursoOpcion(models.Model):
    file = models.FileField(db_column='image_url', blank=False, null=False, upload_to='images/opciones')

    # Foreign Key
    opcion = models.OneToOneField(Opciones, on_delete=models.CASCADE, related_name='RecursoOpcion_opcion')
