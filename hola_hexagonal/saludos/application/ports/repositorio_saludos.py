"""PUERTO DE SALIDA: lo que la aplicacion NECESITA del exterior.

Es un contrato: "necesito guardar y listar saludos, no me importa donde".
Puede ser memoria, MySQL, MariaDB, un archivo... eso lo decide un adaptador.
"""
from abc import ABC, abstractmethod

from saludos.domain.saludo import Saludo


class RepositorioSaludos(ABC):
    @abstractmethod
    def guardar(self, saludo: Saludo) -> None: ...

    @abstractmethod
    def listar(self) -> list[Saludo]: ...
