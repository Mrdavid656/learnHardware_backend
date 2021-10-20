from django.db import models


class RecursoLecciones(models.Model):
    archivo = models.FileField(db_column='image_url', blank=False, null=False, upload_to='images/lecciones')
