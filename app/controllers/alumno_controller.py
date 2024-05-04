from flask import request, jsonify
from ..services import alumno_service

def create_alumno():
    data = request.get_json()
    if 'nombre' not in data:
        return jsonify({'error': 'Falta el nombre del alumno'}), 400
    tutor_id = data.get('tutor_id')  # Optional
    alumno = alumno_service.add_alumno(data['nombre'], tutor_id)
    return jsonify({'id': alumno.id, 'nombre': alumno.nombre}), 201

def get_alumnos():
    alumnos = alumno_service.get_all_alumnos()
    return jsonify([{'id': alumno.id, 'nombre': alumno.nombre} for alumno in alumnos]), 200

def get_alumno_materias(alumno_id):
    materias = alumno_service.get_alumno_materias(alumno_id)
    if materias is not None:
        return jsonify([{'id': materia.id, 'nombre': materia.nombre} for materia in materias]), 200
    return jsonify({'error': 'Alumno no encontrado'}), 404

def assign_tutor_to_alumno(alumno_id):
    data = request.get_json()
    if 'tutor_id' not in data:
        return jsonify({'error': 'Falta el ID del tutor'}), 400
    success = alumno_service.assign_tutor(alumno_id, data['tutor_id'])
    if success:
        return jsonify({'mensaje': 'Tutor asignado correctamente'}), 200
    return jsonify({'error': 'Alumno o tutor no encontrado'}), 404
