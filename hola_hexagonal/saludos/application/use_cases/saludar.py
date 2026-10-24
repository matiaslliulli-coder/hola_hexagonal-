"""CASOS DE USO: la logica de la aplicacion (que pasa cuando alguien pide algo).

Reciben los puertos de salida por el constructor (inyeccion de dependencias),
asi no saben si guardan en memoria o en una base de datos real.
"""
from saludos.application.ports.repositorio_saludos import RepositorioSaludos
from saludos.application.ports.saludar_puerto import (
    ListarSaludosPuerto,
    SaludarPuerto,
)
from saludos.domain.saludo import Saludo


class Saludar(SaludarPuerto):
    def __init__(self, repositorio: RepositorioSaludos):
        self._repositorio = repositorio

    def ejecutar(self, nombre: str) -> Saludo:
        saludo = Saludo.para(nombre)      # reglas del dominio
        self._repositorio.guardar(saludo)  # puerto de salida
        return saludo


class ListarSaludos(ListarSaludosPuerto):
    def __init__(self, repositorio: RepositorioSaludos):
        self._repositorio = repositorio

    def ejecutar(self) -> list[Saludo]:
        return self._repositorio.listar()
