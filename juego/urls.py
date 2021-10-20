from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from juego.api import LeccionViewSet

router = routers.DefaultRouter()
router.register(r'lecciones', LeccionViewSet)
router.register(r'lecciones/recursos', include('recursos.urls'))

urlpatterns = [
    url(r'^', include(router.urls)),
]