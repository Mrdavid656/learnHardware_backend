from rest_framework import serializers, viewsets

from juego.models import Logros


class LogrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logros
        fields = '__all__'


class LogrosViewSet(viewsets.ModelViewSet):
    queryset = Logros.objects.all()
    serializer_class = LogrosSerializer
