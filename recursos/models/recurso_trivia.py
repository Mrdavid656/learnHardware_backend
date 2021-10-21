from django.db import models

from juego.models import Trivia


class RecursoTrivia(models.Model):
    file = models.FileField(db_column='image_url', blank=False, null=False, upload_to='images/trivias')

    # Foreign Key
    trivia = models.OneToOneField(Trivia, on_delete=models.CASCADE, related_name='RecursoTrivia_trivia')
