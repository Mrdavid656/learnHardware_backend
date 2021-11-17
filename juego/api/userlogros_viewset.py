from rest_framework import serializers, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from juego.api import LogrosSerializer
from juego.models import UserLogros, Historial
from juego.repository.logro_logic import logrosGanados


class UserLogrosSerializer(serializers.ModelSerializer):
    logro = LogrosSerializer(many=False, read_only=True)

    class Meta:
        model = UserLogros
        fields = '__all__'


class UserLogrosViewSet(viewsets.ModelViewSet):
    queryset = UserLogros.objects.all()
    serializer_class = UserLogrosSerializer

    @action(detail=False, methods=['post'], url_path="validate", name="Te inserta el premio correspondiente")
    def wonAward(self, request, pk=None):
        if 'usuario' not in request.data:
            return Response('la variable usuario es requerida', status=status.HTTP_400_BAD_REQUEST)
        historial = Historial.objects.all().filter(usuario_id=request.data['usuario'])
        return Response(logrosGanados(historial, request.data['usuario']))
