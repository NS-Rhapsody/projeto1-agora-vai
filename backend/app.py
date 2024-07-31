from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Permitir CORS para todos os domínios na rota /api

@app.route('/api/hello')
def hello():
    return jsonify(message='Funciona porra')

if __name__ == '__main__':
    app.run(debug=True)
