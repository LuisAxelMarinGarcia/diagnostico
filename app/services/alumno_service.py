from ..models.alumno import Alumno
from ..models.materia import Materia
from ..models import db

def add_alumno(nombre, tutor_id=None):
    alumno = Alumno(nombre=nombre, tutor_id=tutor_id)
    db.session.add(alumno)
    db.session.commit()
    return alumno

def get_all_alumnos():
    return Alumno.query.all()

def get_alumno_materias(alumno_id):
    alumno = Alumno.query.get(alumno_id)
    if alumno:
        return alumno.materias
    return None

def assign_tutor(alumno_id, tutor_id):
    alumno = Alumno.query.get(alumno_id)
    if alumno:
        alumno.tutor_id = tutor_id
        db.session.commit()
        return True
    return False
