from rest_framework import serializers, viewsets

from recursos.models import RecursoTrivia


class RecursoTriviaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecursoTrivia
        fields = '__all__'


class RecursoTriviaViewSet(viewsets.ModelViewSet):
    queryset = RecursoTrivia.objects.all()
    serializer_class = RecursoTriviaSerializer
