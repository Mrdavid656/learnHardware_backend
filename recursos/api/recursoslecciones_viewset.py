from rest_framework import serializers, viewsets

from recursos.models import RecursoLecciones


class RecursoLeccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecursoLecciones
        fields = '__all__'


class RecursoLeccionesViewSet(viewsets.ModelViewSet):
    queryset = RecursoLecciones.objects.all()
    serializer_class = RecursoLeccionesSerializer
