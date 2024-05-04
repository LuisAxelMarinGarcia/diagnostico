from . import db

class Materia(db.Model):
    __tablename__ = 'materias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'))

    def __repr__(self):
        return f'<Materia {self.nombre}>'
