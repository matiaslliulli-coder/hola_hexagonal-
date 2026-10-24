"""DOMINIO: la entidad Saludo y sus reglas de negocio.

Aqui NO se importa Django, ni bases de datos, ni nada externo.
Solo Python puro. Si manana cambias de framework, este archivo no se toca.
"""
from dataclasses import dataclass

from saludos.domain.excepciones import NombreInvalido


@dataclass(frozen=True)
class Saludo:
    nombre: str

    def __post_init__(self):
        # Regla de negocio: el nombre no puede venir vacio
        if not self.nombre or not self.nombre.strip():
            raise NombreInvalido("El nombre no puede estar vacio")

    @classmethod
    def para(cls, nombre: str) -> "Saludo":
        # Regla de negocio: el nombre siempre se guarda limpio y en MAYUSCULAS
        return cls(nombre=nombre.strip().upper())

    @property
    def mensaje(self) -> str:
        return f"hola {self.nombre}"
