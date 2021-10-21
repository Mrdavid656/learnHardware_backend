from django.db import models

from juego.models import OpcionesRI


class RecursoOpcionRI(models.Model):
    file = models.FileField(db_column='image_url', blank=False, null=False, upload_to='images/opciones-ri')

    # Foreign Key
    opcion_ri = models.OneToOneField(OpcionesRI, on_delete=models.CASCADE, related_name='RecursoOpcionRI_opcionri')
