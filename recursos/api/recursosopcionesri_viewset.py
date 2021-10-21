from rest_framework import serializers, viewsets

from recursos.models import RecursoOpcionRI


class RecursoOpcionRISerializer(serializers.ModelSerializer):
    class Meta:
        model = RecursoOpcionRI
        fields = '__all__'


class RecursoOpcionViewSet(viewsets.ModelViewSet):
    queryset = RecursoOpcionRI.objects.all()
    serializer_class = RecursoOpcionRISerializer
