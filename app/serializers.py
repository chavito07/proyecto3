from rest_framework import serializers
from .models import Tema, Prerrequisito, RutaAprendizaje, SesionEstudio, ActividadSesion, Repaso

class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields = '__all__'

class PrerrequisitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prerrequisito
        fields = '__all__'

class RutaAprendizajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RutaAprendizaje
        fields = '__all__'

class SesionEstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SesionEstudio
        fields = '__all__'

class ActividadSesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActividadSesion
        fields = '__all__'

class RepasoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repaso
        fields = '__all__'
