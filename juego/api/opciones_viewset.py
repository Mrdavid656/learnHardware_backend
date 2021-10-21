from rest_framework import serializers, viewsets

from juego.models import Opciones


class OpcionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opciones
        fields = '__all__'


class OpcionesViewSet(viewsets.ModelViewSet):
    queryset = Opciones.objects.all()
    serializer_class = OpcionesSerializer
