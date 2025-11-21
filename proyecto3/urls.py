from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Esta función evita que salga el 404 del navegador
def chrome_devtools(request):
    return JsonResponse({})

urlpatterns = [
    path('admin/', admin.site.urls),

    # Ruta de tu aplicación
    path('', include('app.urls')),

    # Ruta para evitar el mensaje del navegador
    path('.well-known/appspecific/com.chrome.devtools.json', chrome_devtools),
]
