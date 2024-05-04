from ..models.materia import Materia
from ..models import db

def add_materia(nombre, alumno_id=None):
    materia = Materia(nombre=nombre, alumno_id=alumno_id)
    db.session.add(materia)
    db.session.commit()
    return materia

def assign_materia_to_alumno(materia_id, alumno_id):
    materia = Materia.query.get(materia_id)
    if materia:
        materia.alumno_id = alumno_id
        db.session.commit()
        return True
    return False
