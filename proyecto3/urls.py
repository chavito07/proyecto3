from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse ,HttpResponseRedirect


# Esta función evita que salga el 404 del navegador
def chrome_devtools(request):
    return JsonResponse({})

urlpatterns = [
    path('api/', include('app.urls')),  # tu app con las APIs
    path('', lambda request: HttpResponseRedirect('/api/')),  # redirección automática
    path('admin/', admin.site.urls),
    # Ruta de tu aplicación
    path('', include('app.urls')),
    # Ruta para evitar el mensaje del navegador
    path('.well-known/appspecific/com.chrome.devtools.json', chrome_devtools),
]
