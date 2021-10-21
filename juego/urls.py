from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from juego.api import LeccionViewSet, NivelesActividadesViewSet, TriviaViewset, OpcionesViewSet, \
    ReconocimientoImagenesViewSet, OpcionesRIViewSet

router = routers.DefaultRouter()
router.register(r'lecciones', LeccionViewSet)
router.register(r'lecciones/actividades', NivelesActividadesViewSet)
router.register(r'trivias', TriviaViewset)
router.register(r'opciones', OpcionesViewSet)
router.register(r'reconocimiento_imagenes', ReconocimientoImagenesViewSet)
router.register(r'opciones-ri', OpcionesRIViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('lecciones/recursos', include('recursos.urls')),
]
