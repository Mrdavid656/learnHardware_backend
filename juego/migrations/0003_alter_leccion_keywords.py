# Generated by Django 3.2.8 on 2021-11-10 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0002_historial_nivelesactividades_opciones_opcionesri_reconocimientoimagenes_trivia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leccion',
            name='keywords',
            field=models.CharField(max_length=100),
        ),
    ]
