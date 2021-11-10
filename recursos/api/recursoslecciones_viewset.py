from rest_framework import serializers, viewsets
from rest_framework.decorators import action

from base.utils import CommonResponseUtil
from juego.api import LeccionSimpleSerializer
from juego.models import Leccion
from recursos.models import RecursoLecciones


class RecursoLeccionesSerializer(serializers.ModelSerializer):
    leccion = LeccionSimpleSerializer(many=False, read_only=True)
    leccion_id = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset=Leccion.objects.all(), source='leccion')

    class Meta:
        model = RecursoLecciones
        fields = '__all__'


class RecursoLeccionesViewSet(viewsets.ModelViewSet):
    queryset = RecursoLecciones.objects.all()
    serializer_class = RecursoLeccionesSerializer
