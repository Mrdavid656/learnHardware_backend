# Generated by Django 3.2.8 on 2021-11-10 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0003_alter_leccion_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='leccion',
            name='categoria',
            field=models.PositiveSmallIntegerField(choices=[(0, 'novato'), (1, 'sabiondo'), (2, 'estrella')], default=0),
        ),
    ]
