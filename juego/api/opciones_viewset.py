from rest_framework import serializers, viewsets

from juego.models import Opciones
from recursos.api import RecursoOpcionSerializer


class OpcionesSerializer(serializers.ModelSerializer):
    recurso = RecursoOpcionSerializer(many=False, read_only=True, source='RecursoOpcion_opcion')

    class Meta:
        model = Opciones
        fields = '__all__'


class OpcionesViewSet(viewsets.ModelViewSet):
    queryset = Opciones.objects.all()
    serializer_class = OpcionesSerializer
