from django.urls import path
from .views import PersonaAPI

urlpatterns = [
    path('persona/', PersonaAPI.as_view(), name='crear_persona'),
    path('persona/<int:persona_id>/', PersonaAPI.as_view(), name='obtener_persona'),
]
