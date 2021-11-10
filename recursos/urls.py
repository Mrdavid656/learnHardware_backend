from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from recursos.api import RecursoLeccionesViewSet, RecursoTriviaViewSet, RecursoOpcionViewSet

router = routers.DefaultRouter()
router.register(r'lecciones', RecursoLeccionesViewSet)
router.register(r'trivias', RecursoTriviaViewSet)
router.register(r'opciones', RecursoOpcionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
