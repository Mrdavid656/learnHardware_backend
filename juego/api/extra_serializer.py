from rest_framework import serializers

from juego.models import Leccion, Trivia


class LeccionSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccion
        fields = ['id', 'titulo']


class TriviaSimpleSerializer(serializers.ModelSerializer):
    leccion = LeccionSimpleSerializer(many=False, read_only=True)

    class Meta:
        model = Trivia
        fields = ['leccion', 'pregunta']
