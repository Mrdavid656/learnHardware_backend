from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from recursos.api import RecursoLeccionesViewSet, RecursoTriviaViewSet, RecursoOpcionViewSet, \
    RecursosHasLeccionesViewSet

router = routers.DefaultRouter()
router.register(r'recursos-lecciones', RecursoLeccionesViewSet)
router.register(r'recursos/lecciones', RecursosHasLeccionesViewSet)
router.register(r'recursos-trivias', RecursoTriviaViewSet)
router.register(r'recursos-opciones', RecursoOpcionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
