from flask import request, jsonify
from ..services import materia_service

def create_materia():
    data = request.get_json()
    if 'nombre' not in data:
        return jsonify({'error': 'Falta el nombre de la materia'}), 400
    alumno_id = data.get('alumno_id')  
    materia = materia_service.add_materia(data['nombre'], alumno_id)
    return jsonify({'id': materia.id, 'nombre': materia.nombre}), 201

def assign_materia_to_alumno(materia_id):
    data = request.get_json()
    if 'alumno_id' not in data:
        return jsonify({'error': 'Falta el ID del alumno'}), 400
    success = materia_service.assign_materia_to_alumno(materia_id, data['alumno_id'])
    if success:
        return jsonify({'mensaje': 'Materia asignada correctamente'}), 200
    return jsonify({'error': 'Materia o alumno no encontrado'}), 404
