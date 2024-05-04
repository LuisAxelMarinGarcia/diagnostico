from flask import request, jsonify
from ..services import tutor_service

def create_tutor():
    data = request.get_json()
    if 'nombre' not in data:
        return jsonify({'error': 'Falta el nombre del tutor'}), 400
    tutor = tutor_service.add_tutor(data['nombre'])
    return jsonify({'id': tutor.id, 'nombre': tutor.nombre}), 201

def get_tutors():
    tutores = tutor_service.get_all_tutors()
    return jsonify([{'id': tutor.id, 'nombre': tutor.nombre} for tutor in tutores]), 200

def get_tutor_alumnos(tutor_id):
    alumnos = tutor_service.get_tutor_alumnos(tutor_id)
    if alumnos is not None:
        return jsonify([{'id': alumno.id, 'nombre': alumno.nombre} for alumno in alumnos]), 200
    return jsonify({'error': 'Tutor no encontrado'}), 404
