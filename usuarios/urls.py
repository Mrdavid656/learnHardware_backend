from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from usuarios.api import UserViewset

router = routers.DefaultRouter()
router.register(r'usuarios', UserViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
]