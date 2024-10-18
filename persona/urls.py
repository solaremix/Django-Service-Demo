from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_personas, name='listar_personas'),
]
