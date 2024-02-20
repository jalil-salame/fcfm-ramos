from dataclasses import dataclass

from fcfmramos.web_scraper.config import FCFM_CATALOGO_URL, FCFM_SALAS_URL

# TODO: implement
# @dataclass
# class Horario:
#     tipo: str
#     dia: str
#     hora_inicio: str
#     hora_termino: str


@dataclass
class Profesor:
    ucampus_id: str
    nombre: str


@dataclass
class Curso:
    seccion: int
    cupos: int
    cupos_ocupados: int
    programa_id: int
    modalidad: str
    comentario: str
    profesores: list[Profesor]
    # horarios: list[Horario]
    horarios: str


@dataclass
class Ramo:
    codigo: str
    nombre: str
    sct: int
    comentario: str | None
    sustentabilidad: bool
    requisitos: str
    equivalencias: list[str] | None
    secciones: list[Curso]


@dataclass
class Departamento:
    id: int
    nombre: str
    codigo: str
    color: str


@dataclass
class Catalogo:
    semestre: int
    departamento: Departamento
    ramos: list[Ramo]


def get_sala_url(sala: int) -> str:
    return f"{FCFM_SALAS_URL}{sala}"


def get_catalogo_url(semester: int, department: int) -> str:
    return f"{FCFM_CATALOGO_URL}?semestre={semester}&depto={department}"
