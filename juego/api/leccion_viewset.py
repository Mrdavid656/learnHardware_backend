from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from base.repository import validatePk
from base.utils import CommonResponseUtil
from juego.api import TriviaSerializer
from juego.models import Leccion, Trivia
from recursos.models import RecursoLecciones


class LeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccion
        fields = '__all__'


class LeccionViewSet(viewsets.ModelViewSet):
    queryset = Leccion.objects.all()
    serializer_class = LeccionSerializer

    @action(detail=True, methods=['get'], url_path="recursos", name="Obtener imagenes de una leccion")
    def recursosByLeccion(self, request, pk=None):
        try:
            validatePk(pk, Leccion)
        except:
            return CommonResponseUtil.response_not_found()
        else:
            queryset = RecursoLecciones.objects.filter(leccion_id=pk)
            page = self.paginate_queryset(queryset)
            from recursos.api import RecursoLeccionesSerializer
            if page is not None:
                serializer = RecursoLeccionesSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = RecursoLeccionesSerializer(queryset, many=True)
            return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path="preguntas", name="Obtener preguntas de una leccion")
    def preguntasByLeccion(self, request, pk=None):
        try:
            validatePk(pk, Leccion)
        except:
            return CommonResponseUtil.response_not_found()
        else:
            queryset = Trivia.objects.filter(leccion_id=pk)
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = TriviaSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = TriviaSerializer(queryset, many=True)
            return Response(serializer.data)
