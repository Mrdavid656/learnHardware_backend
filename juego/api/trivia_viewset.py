from rest_framework import serializers, viewsets

from juego.models import Trivia


class TriviaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trivia
        fields = '__all__'


class TriviaViewset(viewsets.ModelViewSet):
    queryset = Trivia.objects.all()
    serializer_class = TriviaSerializer
