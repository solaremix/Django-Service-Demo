from django.http import JsonResponse, Http404
from .models import Persona
from django.views import View
import json

class PersonaAPI(View):

    def post(self, request):
        data = json.loads(request.body)
        persona = Persona.objects.create(**data)
        return JsonResponse({"mensaje": "Persona creada con éxito", "persona": persona.nombre})

    def get(self, request, persona_id=None):
        if persona_id:
            try:
                persona = Persona.objects.get(id=persona_id)
                return JsonResponse({
                    "nombre": persona.nombre,
                    "apellido": persona.apellido,
                    "edad": persona.edad,
                    "genero": persona.genero,
                    "fecha_nacimiento": persona.fecha_nacimiento,
                    "dni": persona.dni,
                    "direccion": persona.direccion,
                })
            except Persona.DoesNotExist:
                return JsonResponse({"error": "Persona no encontrada"}, status=404)
        else:
            personas = list(Persona.objects.values())
            return JsonResponse(personas, safe=False)
