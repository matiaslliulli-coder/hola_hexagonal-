from django.test import SimpleTestCase

from saludos.application.use_cases.saludar import Saludar
from saludos.domain.excepciones import NombreInvalido
from saludos.infrastructure.outbound.repositorio_memoria import RepositorioMemoria


class PruebasDelCasoDeUso(SimpleTestCase):
    """Prueban el hexagono SIN levantar HTTP: por eso la arquitectura es util."""

    def test_saluda_en_mayusculas(self):
        caso = Saludar(RepositorioMemoria())
        self.assertEqual(caso.ejecutar("matias").mensaje, "hola MATIAS")

    def test_nombre_vacio_falla(self):
        with self.assertRaises(NombreInvalido):
            Saludar(RepositorioMemoria()).ejecutar("   ")


class PruebasHTTP(SimpleTestCase):
    def test_get(self):
        r = self.client.get("/saludar/matias/")
        self.assertEqual(r.json(), {"mensaje": "hola MATIAS"})

    def test_post(self):
        r = self.client.post(
            "/saludar/", {"nombre": "Matias"}, content_type="application/json"
        )
        self.assertEqual(r.json(), {"mensaje": "hola MATIAS"})
