from . import db

class Disciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=True, nullable=False)
    possivelProfessor = db.Column(db.String(120), unique=True, nullable=False)
    preRequisitos = db.Column(db.String(120), unique=True, nullable=False)
    necessidades = db.Column(db.String(120), unique=True, nullable=False)
    obrigatorio = db.Column(db.Boolean, unique=True, nullable=False)
    eletiva = db.Column(db.Boolean, unique=True, nullable=False)
    optativa = db.Column(db.Boolean, unique=True, nullable=False)
    semestre = db.Column(db.String(2), unique=True, nullable=False)
    curso = db.Column(db.String(120), unique=True, nullable=False)

class Sala(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomeSala = db.Column(db.String(64), unique=True, nullable=False)
    tipo = db.Column(db.String(120), unique=True, nullable=False)

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=True, nullable=False)
    possivelOferta = db.Column(db.String(120), unique=True, nullable=False)

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idDisciplina = db.Column(db.Integer, unique=True, nullable=False)
    idProfessor = db.Column(db.Integer, unique=True, nullable=False)
    idSala = db.Column(db.Integer, unique=True, nullable=False)