# Generated by Django 3.2.8 on 2021-11-10 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0004_leccion_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='leccion',
            name='resumen',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
