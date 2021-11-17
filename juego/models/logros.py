from django.db import models


class Logros(models.Model):
    FIRST_GAME_PLAYED = 0
    WELCOME_SABIONDO_DIFICULTY = 1
    WELCOME_EXPERTO_DIFICULTY = 2
    PERFECT_LESSON_PLAYED = 3
    RAZON_TYPES_CHOICES = (
        (FIRST_GAME_PLAYED, 'first_game'),
        (WELCOME_SABIONDO_DIFICULTY, 'sabiondo'),
        (WELCOME_EXPERTO_DIFICULTY, 'experto'),
        (PERFECT_LESSON_PLAYED, 'perfecto'),
    )

    nombre = models.CharField(max_length=200)
    motivo = models.CharField(max_length=500)
    razon = models.PositiveSmallIntegerField()
    icon = models.FileField(db_column='image_url', blank=False, null=False, upload_to='images/logros')