from rest_framework import serializers, viewsets

from recursos.models import RecursosHasLecciones


class RecursosHasLeccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecursosHasLecciones
        fields = '__all__'


class RecursosHasLeccionesViewSet(viewsets.ModelViewSet):
    queryset = RecursosHasLecciones.objects.all()
    serializer_class = RecursosHasLeccionesSerializer
