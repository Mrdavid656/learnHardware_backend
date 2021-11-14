from django.db import transaction
from rest_framework import serializers, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from juego.api.extra_serializer import TriviaSimpleSerializer
from juego.models import Historial, Trivia
from usuarios.models import UserProfile, Nivel
from usuarios.repositories import isUserLevelUp


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
        arguments = {
            'puntos': request.data['puntos'],
            'usuario': request.data['usuario'],
        }
        models = {
            'Nivel': Nivel,
            'UserProfile': UserProfile
        }
        if isUserLevelUp(arguments, models) is True:
            return Response({'levelup': 'user is levelUp'}, status=status.HTTP_201_CREATED)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['post'], url_path="lecciones", name="Obtener todas las lecciones de un usuario")
    def historialByUser(self, request, pk=None):
        if 'usuario' not in request.data:
            return Response('variable usuario is required', status=status.HTTP_400_BAD_REQUEST)
        queryset = Historial.objects.filter(usuario_id=request.data['usuario']).order_by('-date')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = HistorialSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = HistorialSerializer(queryset, many=True)
        return Response(serializer.data)

