from . import db

class Alumno(db.Model):
    __tablename__ = 'alumnos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutores.id'))
    materias = db.relationship('Materia', backref='alumno', lazy='dynamic')

    def __repr__(self):
        return f'<Alumno {self.nombre}>'
