"""ADAPTADOR DE ENTRADA: traduce HTTP (Django) <-> casos de uso.

Solo hace 3 cosas: leer la peticion, llamar al caso de uso, devolver JSON.
No tiene logica de negocio.
"""
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from saludos.domain.excepciones import NombreInvalido
from saludos.infrastructure import contenedor


@require_http_methods(["GET"])
def saludar_por_url(request, nombre):
    """GET /saludar/matias/  ->  {"mensaje": "hola MATIAS"}"""
    try:
        saludo = contenedor.saludar.ejecutar(nombre)
    except NombreInvalido as error:
        return JsonResponse({"error": str(error)}, status=400)
    return JsonResponse({"mensaje": saludo.mensaje})


@csrf_exempt
@require_http_methods(["POST"])
def saludar_por_json(request):
    """POST /saludar/ con {"nombre": "matias"}  ->  {"mensaje": "hola MATIAS"}"""
    try:
        datos = json.loads(request.body or "{}")
        saludo = contenedor.saludar.ejecutar(datos.get("nombre", ""))
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON invalido"}, status=400)
    except NombreInvalido as error:
        return JsonResponse({"error": str(error)}, status=400)
    return JsonResponse({"mensaje": saludo.mensaje})


@require_http_methods(["GET"])
def historial(request):
    """GET /saludos/  ->  lista de todos los saludos hechos."""
    saludos = contenedor.listar_saludos.ejecutar()
    return JsonResponse({"saludos": [s.mensaje for s in saludos]})
