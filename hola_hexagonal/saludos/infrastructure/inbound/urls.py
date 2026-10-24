from django.urls import path

from saludos.infrastructure.inbound import vistas

urlpatterns = [
    path("saludar/", vistas.saludar_por_json, name="saludar-json"),
    path("saludar/<str:nombre>/", vistas.saludar_por_url, name="saludar-url"),
    path("saludos/", vistas.historial, name="historial"),
]
