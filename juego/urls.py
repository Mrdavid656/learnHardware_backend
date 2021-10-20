from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from juego.api import LeccionViewSet

router = routers.DefaultRouter()
router.register(r'lecciones', LeccionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('lecciones/recursos', include('recursos.urls')),
]
