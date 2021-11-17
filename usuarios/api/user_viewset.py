from rest_framework import serializers, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from base.repository import validatePk
from base.utils import CommonResponseUtil
from juego.api import UserLogrosSerializer
from juego.models import UserLogros
from usuarios.api import NivelSimpleSerializer
from usuarios.models import UserProfile, Nivel
from usuarios.repositories import create_user


class UserProfileSerializer(serializers.ModelSerializer):
    nivel = NivelSimpleSerializer(many=False, read_only=True)
    nivel_id = serializers.PrimaryKeyRelatedField(
        many=False, write_only=True, queryset=Nivel.objects.all(), source='nivel'
    )

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserRegisterSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=200)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)

    class Meta:
        fields = "__all__"


class UserViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data, context={'request': self.request})
        if serializer.is_valid():
            user = create_user(request, UserProfile, Nivel)
            return Response(UserProfileSerializer(user, many=False).data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], url_path="logros", name="Obtener logros de un usuario")
    def preguntasByLeccion(self, request, pk=None):
        try:
            validatePk(pk, UserProfile)
        except:
            return CommonResponseUtil.response_not_found()
        else:
            queryset = UserLogros.objects.filter(usuario_id=pk)
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = UserLogrosSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = UserLogrosSerializer(queryset, many=True)
            return Response(serializer.data)

