from django.db import models

from juego.models import ReconocimientoImagenes


class OpcionesRI(models.Model):
    opcion = models.CharField(max_length=200)
    opcion_correcta = models.BooleanField(default=False)

    # Foreign Key
    reconocimiento_imagenes = models.ForeignKey(
        ReconocimientoImagenes, on_delete=models.CASCADE, related_name='OpcionesRI_reconocimientoimagenes')
