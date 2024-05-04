from ..models.tutor import Tutor
from ..models import db

def add_tutor(nombre):
    tutor = Tutor(nombre=nombre)
    db.session.add(tutor)
    db.session.commit()
    return tutor

def get_all_tutors():
    return Tutor.query.all()

def get_tutor_alumnos(tutor_id):
    tutor = Tutor.query.get(tutor_id)
    if tutor:
        return tutor.alumnos
    return None
