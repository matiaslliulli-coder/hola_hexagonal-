"""RAIZ DE COMPOSICION: aqui se "enchufan" los adaptadores a los puertos.

Es el UNICO lugar que conoce todas las piezas. Si quieres cambiar
RepositorioMemoria por uno de base de datos, lo cambias aqui y nada mas.
"""
from saludos.application.use_cases.saludar import ListarSaludos, Saludar
from saludos.infrastructure.outbound.repositorio_memoria import RepositorioMemoria

_repositorio = RepositorioMemoria()

saludar = Saludar(_repositorio)
listar_saludos = ListarSaludos(_repositorio)
