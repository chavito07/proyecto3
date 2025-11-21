from django.urls import path, include
from rest_framework import routers
from .views import (
    TemaViewSet, PrerrequisitoViewSet, RutaAprendizajeViewSet,
    SesionEstudioViewSet, ActividadSesionViewSet, RepasoViewSet
)

router = routers.DefaultRouter()
router.register('temas', TemaViewSet)
router.register('prerrequisitos', PrerrequisitoViewSet)
router.register('rutas', RutaAprendizajeViewSet)
router.register('sesiones', SesionEstudioViewSet)
router.register('actividades', ActividadSesionViewSet)
router.register('repasos', RepasoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
