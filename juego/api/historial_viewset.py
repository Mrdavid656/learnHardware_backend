from rest_framework import serializers, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from juego.api.extra_serializer import TriviaSimpleSerializer
from juego.models import Historial, Trivia
from usuarios.models import UserProfile, Nivel


class HistorialSerializer(serializers.ModelSerializer):
    trivia = TriviaSimpleSerializer(many=False, read_only=True)
    trivia_id = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset=Trivia.objects.all(), source='trivia')

    class Meta:
        model = Historial
        fields = '__all__'


class HistorialViewSet(viewsets.ModelViewSet):
    queryset = Historial.objects.all()
    serializer_class = HistorialSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        if (request.data['puntos'] > 0):
            usuario = UserProfile.objects.filter(id=request.data['usuario']).first()
            usuario.puntos += request.data['puntos']
            nivel = Nivel.objects.filter(id=usuario.nivel_id).first()
            if usuario.puntos >= nivel.limite_puntos:
                niveles = Nivel.objects.all().order_by('id')
                usuario.nivel = niveles[int(nivel.nombre)]
                usuario.puntos = 0
                usuario.save()
                return Response({'levelup': niveles[int(nivel.nombre)]}, status=status.HTTP_201_CREATED)
            usuario.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['post'], url_path="lecciones", name="Obtener todas las lecciones de un usuario")
    def historialByUser(self, request, pk=None):
        if 'usuario' not in request.data:
            return Response('variable usuario is required', status=status.HTTP_400_BAD_REQUEST)
        queryset = Historial.objects.filter(usuario_id=request.data['usuario']).order_by('trivia')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = HistorialSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = HistorialSerializer(queryset, many=True)
        return Response(serializer.data)

