"""PUERTO DE ENTRADA: lo que la aplicacion OFRECE al mundo exterior.

Es un contrato: "yo se saludar". Quien lo llame (HTTP, consola, tests)
solo necesita conocer esta interfaz.
"""
from abc import ABC, abstractmethod

from saludos.domain.saludo import Saludo


class SaludarPuerto(ABC):
    @abstractmethod
    def ejecutar(self, nombre: str) -> Saludo: ...


class ListarSaludosPuerto(ABC):
    @abstractmethod
    def ejecutar(self) -> list[Saludo]: ...
