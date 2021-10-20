from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from recursos.api import RecursoLeccionesViewSet
from recursos.api.recursoshaslecciones_viewset import RecursosHasLeccionesViewSet

router = routers.DefaultRouter()
router.register(r'recursos-lecciones', RecursoLeccionesViewSet)
router.register(r'recursos/lecciones', RecursosHasLeccionesViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]