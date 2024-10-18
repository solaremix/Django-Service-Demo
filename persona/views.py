from django.shortcuts import render
from .models import Persona

def listar_personas(request):
    personas = Persona.objects.all()
    return render(request, 'persona/listar_personas.html', {'personas': personas})
