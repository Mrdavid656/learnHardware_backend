from rest_framework import serializers, viewsets

from juego.models import ReconocimientoImagenes


class ReconocimientoImagenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReconocimientoImagenes
        fields = '__all__'


class ReconocimientoImagenesViewSet(viewsets.ModelViewSet):
    queryset = ReconocimientoImagenes.objects.all()
    serializer_class = ReconocimientoImagenesSerializer
