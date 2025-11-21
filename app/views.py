from rest_framework import viewsets
from .models import Tema, Prerrequisito, RutaAprendizaje, SesionEstudio, ActividadSesion, Repaso
from .serializers import (
    TemaSerializer, PrerrequisitoSerializer, RutaAprendizajeSerializer,
    SesionEstudioSerializer, ActividadSesionSerializer, RepasoSerializer
)

# API CRUD para cada modelo
class TemaViewSet(viewsets.ModelViewSet):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer

class PrerrequisitoViewSet(viewsets.ModelViewSet):
    queryset = Prerrequisito.objects.all()
    serializer_class = PrerrequisitoSerializer

class RutaAprendizajeViewSet(viewsets.ModelViewSet):
    queryset = RutaAprendizaje.objects.all()
    serializer_class = RutaAprendizajeSerializer

class SesionEstudioViewSet(viewsets.ModelViewSet):
    queryset = SesionEstudio.objects.all()
    serializer_class = SesionEstudioSerializer

class ActividadSesionViewSet(viewsets.ModelViewSet):
    queryset = ActividadSesion.objects.all()
    serializer_class = ActividadSesionSerializer

class RepasoViewSet(viewsets.ModelViewSet):
    queryset = Repaso.objects.all()
    serializer_class = RepasoSerializer
