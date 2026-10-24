"""ADAPTADOR DE SALIDA: implementacion concreta del repositorio.

Guarda los saludos en una lista en memoria (se borran al apagar el servidor).
Para usar una base de datos real, creas otro adaptador (por ejemplo
repositorio_django_orm.py) que herede de RepositorioSaludos y listo:
no se cambia ni el dominio ni los casos de uso.
"""
from saludos.application.ports.repositorio_saludos import RepositorioSaludos
from saludos.domain.saludo import Saludo


class RepositorioMemoria(RepositorioSaludos):
    def __init__(self):
        self._saludos: list[Saludo] = []

    def guardar(self, saludo: Saludo) -> None:
        self._saludos.append(saludo)

    def listar(self) -> list[Saludo]:
        return list(self._saludos)
