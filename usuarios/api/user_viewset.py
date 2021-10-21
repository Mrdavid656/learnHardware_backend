from rest_framework import serializers, viewsets, status
from rest_framework.response import Response

from usuarios.api import NivelSimpleSerializer
from usuarios.models import UserProfile, Nivel


class UserProfileSerializer(serializers.ModelSerializer):
    nivel = NivelSimpleSerializer(many=False, read_only=True)
    nivel_id = serializers.PrimaryKeyRelatedField(
        many=False, write_only=True, queryset=Nivel.objects.all(), source='nivel'
    )

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=200)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    nivel_id = serializers.PrimaryKeyRelatedField(
        many=False, write_only=True, queryset=Nivel.objects.all(), source='nivel'
    )

    class Meta:
        fields = "__all__"


class UserViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data, context={'request': self.request})
        if serializer.is_valid():
            user = UserProfile()
            user.first_name = serializer.data['first_name']
            user.last_name = serializer.data['last_name']
            user.email = serializer.data['email']
            user.username = serializer.data['username']
            user.set_password(serializer.data['password'])
            user.nivel = Nivel.objects.filter(id=serializer.initial_data['nivel_id']).first()
            user.puntos = serializer.data['puntos'] if 'puntos' in serializer.data else 0

            user.save()
            return Response(UserProfileSerializer(user, many=False).data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
