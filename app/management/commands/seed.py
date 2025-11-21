from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Tema, Prerrequisito, RutaAprendizaje, SesionEstudio, ActividadSesion, Repaso

class Command(BaseCommand):
    help = "Llena la base de datos con datos iniciales en todas las tablas"

    def handle(self, *args, **kwargs):
        # Crear usuario de prueba
        usuario, created = User.objects.get_or_create(
            username="kevin",
            defaults={"email": "kevin@example.com", "password": "12345"}
        )

        # Crear temas
        tema1 = Tema.objects.create(
            titulo="Introducción a Listas",
            descripcion="Conceptos básicos de listas en Python",
            nivel_dificultad=1,
            puntos=10
        )
        tema2 = Tema.objects.create(
            titulo="Árboles Binarios",
            descripcion="Estructura jerárquica para organizar datos",
            nivel_dificultad=3,
            puntos=20
        )
        tema3 = Tema.objects.create(
            titulo="Colas y Pilas",
            descripcion="Estructuras lineales fundamentales",
            nivel_dificultad=2,
            puntos=15
        )

        # Crear prerrequisitos
        Prerrequisito.objects.create(origen=tema1, destino=tema2, tipo="necesario")
        Prerrequisito.objects.create(origen=tema1, destino=tema3, tipo="recomendado")

        # Crear ruta de aprendizaje
        ruta1 = RutaAprendizaje.objects.create(usuario=usuario, tema=tema1, completado=True)
        ruta2 = RutaAprendizaje.objects.create(usuario=usuario, tema=tema2, padre=ruta1, completado=False)
        ruta3 = RutaAprendizaje.objects.create(usuario=usuario, tema=tema3, padre=ruta1, completado=False)

        # Crear sesión de estudio
        sesion = SesionEstudio.objects.create(usuario=usuario, tema=tema1)

        ActividadSesion.objects.create(
            sesion=sesion,
            tipo="explicación",
            contenido="Repaso teórico de listas",
            orden=1
        )
        ActividadSesion.objects.create(
            sesion=sesion,
            tipo="ejercicio",
            contenido="Resolver problemas prácticos con listas",
            orden=2
        )

        # Crear repasos
        Repaso.objects.create(usuario=usuario, tema=tema2, prioridad=1)
        Repaso.objects.create(usuario=usuario, tema=tema3, prioridad=2)

        self.stdout.write(self.style.SUCCESS("Datos iniciales insertados en todas las tablas"))