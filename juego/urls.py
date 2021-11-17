from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from juego.api import LeccionViewSet, TriviaViewset, OpcionesViewSet, HistorialViewSet, LogrosViewSet, UserLogrosViewSet

router = routers.DefaultRouter()
router.register(r'lecciones', LeccionViewSet)
router.register(r'trivias', TriviaViewset)
router.register(r'opciones', OpcionesViewSet)
router.register(r'historial', HistorialViewSet)
router.register(r'logros', LogrosViewSet)
router.register(r'user/logros', UserLogrosViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('lecciones/recursos', include('recursos.urls')),
]
