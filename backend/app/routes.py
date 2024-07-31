from flask import current_app as app, jsonify, request
from .models import Sala
from . import db

@app.route('/api/salas', methods=['GET'])
def get_salas():
    salas = Sala.query.all()
    return jsonify([{'id': sala.id, 'nomeSala': sala.nomeSala, 'tipo': sala.tipo} for sala in salas])

@app.route('/api/salas', methods=['POST'])
def add_sala():
    data = request.get_json()
    new_sala = Sala(nomeSala=data['nomeSala'], tipo=data['tipo'])
    db.session.add(new_sala)
    db.session.commit()
    return jsonify({'message': 'sala adicionada'}), 201
