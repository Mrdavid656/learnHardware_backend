from django.db import models


class Leccion(models.Model):
    titulo = models.CharField(max_length=200)
    informacion = models.TextField()

    # Foreign Key
    keywords = models.IntegerField()
