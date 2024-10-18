from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('persona/', include('persona.urls')),  # Ruta de la app 'persona'
]
