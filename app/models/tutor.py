from . import db

class Tutor(db.Model):
    __tablename__ = 'tutores'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    alumnos = db.relationship('Alumno', backref='tutor', lazy='dynamic')

    def __repr__(self):
        return f'<Tutor {self.nombre}>'
