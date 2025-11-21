from django.db import models
from django.contrib.auth.models import User

# Modelo para representar los TEMAS (nodos del grafo)
class Tema(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    nivel_dificultad = models.IntegerField(default=1)  # 1–5
    puntos = models.IntegerField(default=10)

    def __str__(self):
        return self.titulo

class Prerrequisito(models.Model):
    origen = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name="tema_origen")
    destino = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name="tema_destino")
    tipo = models.CharField(max_length=20, default="normal")  # Ej: "necesario", "recomendado"

    def __str__(self):
        return f"{self.origen} → {self.destino}"

class RutaAprendizaje(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    padre = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="hijos")
    completado = models.BooleanField(default=False)

# Modelo para sesiones de estudio (LISTA / ORDEN)
class SesionEstudio(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)

class ActividadSesion(models.Model):
    sesion = models.ForeignKey(SesionEstudio, on_delete=models.CASCADE, related_name="actividades")
    tipo = models.CharField(max_length=20)  # explicación, reto, ejercicio
    contenido = models.TextField()
    orden = models.IntegerField()  # lista ordenada

# Modelo para REPASO tipo spaced repetition (PILA o COLA)
class Repaso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    prioridad = models.IntegerField(default=1)  # 1 = más urgente
    fecha_agregado = models.DateTimeField(auto_now_add=True)
