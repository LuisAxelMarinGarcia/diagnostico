from flask import Flask
from .controllers.tutor_controller import create_tutor, get_tutors, get_tutor_alumnos
from .controllers.alumno_controller import create_alumno, get_alumnos, get_alumno_materias, assign_tutor_to_alumno
from .controllers.materia_controller import create_materia, assign_materia_to_alumno

def init_routes(app):
    # Rutas para Tutores
    app.add_url_rule('/tutores', 'create_tutor', create_tutor, methods=['POST'])
    app.add_url_rule('/tutores', 'get_tutors', get_tutors, methods=['GET'])
    app.add_url_rule('/tutores/<int:tutor_id>/alumnos', 'get_tutor_alumnos', get_tutor_alumnos, methods=['GET'])

    # Rutas para Alumnos
    app.add_url_rule('/alumnos', 'create_alumno', create_alumno, methods=['POST'])
    app.add_url_rule('/alumnos', 'get_alumnos', get_alumnos, methods=['GET'])
    app.add_url_rule('/alumnos/<int:alumno_id>/materias', 'get_alumno_materias', get_alumno_materias, methods=['GET'])
    app.add_url_rule('/alumnos/<int:alumno_id>/tutor', 'assign_tutor_to_alumno', assign_tutor_to_alumno, methods=['POST'])

    # Rutas para Materias
    app.add_url_rule('/materias', 'create_materia', create_materia, methods=['POST'])
    app.add_url_rule('/materias/<int:materia_id>/alumno', 'assign_materia_to_alumno', assign_materia_to_alumno, methods=['POST'])
