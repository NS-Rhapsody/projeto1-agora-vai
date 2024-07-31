from . import db

class Sala(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomeSala = db.Column(db.String(64), unique=True, nullable=False)
    tipo = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Sala {self.nomeSala}>'