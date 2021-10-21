from rest_framework import serializers

from usuarios.models import Nivel


class NivelSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel
        fields = ['id', 'nombre']