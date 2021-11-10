from rest_framework import serializers, viewsets

from juego.api import OpcionesSerializer
from juego.models import Trivia
from recursos.api import RecursoTriviaSerializer


class TriviaSerializer(serializers.ModelSerializer):
    opciones = OpcionesSerializer(many=True, read_only=True, source='Opciones_trivia')
    recurso = RecursoTriviaSerializer(many=True, read_only=True, source='RecursoTrivia_trivia')

    class Meta:
        model = Trivia
        fields = '__all__'


class TriviaViewset(viewsets.ModelViewSet):
    queryset = Trivia.objects.all()
    serializer_class = TriviaSerializer
