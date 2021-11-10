from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from juego.api import LeccionViewSet, TriviaViewset, OpcionesViewSet, HistorialViewSet

router = routers.DefaultRouter()
router.register(r'lecciones', LeccionViewSet)
router.register(r'trivias', TriviaViewset)
router.register(r'opciones', OpcionesViewSet)
router.register(r'historial', HistorialViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('lecciones/recursos', include('recursos.urls')),
]
