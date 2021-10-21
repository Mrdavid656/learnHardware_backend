from rest_framework import serializers, viewsets

from juego.models import NivelesActividades


class NivelesActividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelesActividades
        fields = '__all__'


class NivelesActividadesViewSet(viewsets.ModelViewSet):
    queryset = NivelesActividades.objects.all()
    serializer_class = NivelesActividadesSerializer
