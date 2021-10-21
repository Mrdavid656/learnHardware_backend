from rest_framework import serializers, viewsets

from juego.models import OpcionesRI


class OpcionesRISerializer(serializers.ModelSerializer):
    class Meta:
        model = OpcionesRI
        fields = '__all__'


class OpcionesRIViewSet(viewsets.ModelViewSet):
    queryset = OpcionesRI.objects.all()
    serializer_class = OpcionesRISerializer
