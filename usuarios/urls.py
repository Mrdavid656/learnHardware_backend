from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from usuarios.api import UserViewset, NivelViewset

router = routers.DefaultRouter()
router.register(r'usuarios', UserViewset)
router.register(r'niveles', NivelViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
]
