from rest_framework import serializers, viewsets

from recursos.models import RecursoOpcion


class RecursoOpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecursoOpcion
        fields = '__all__'


class RecursoOpcionViewSet(viewsets.ModelViewSet):
    queryset = RecursoOpcion.objects.all()
    serializer_class = RecursoOpcionSerializer
