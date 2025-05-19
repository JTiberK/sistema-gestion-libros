from flask import Blueprint, request, jsonify
from models.usuario import Usuario, Moderador, Admin, login

auth_bp = Blueprint('auth', __name__, url_prefix='/api')

@auth_bp.route('/login', methods=['POST'])
def login_route():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    rol = data.get('rol', 'usuario')

    roles = {
        'usuario': Usuario,
        'moderador': Moderador,
        'admin': Admin
    }

    clase = roles.get(rol.lower())
    if not clase:
        return jsonify({'error': 'Rol inválido'}), 400

    usuario = clase(username, password)
    if login(usuario, password):
        return jsonify({'token': 'fake-jwt'}), 200
    else:
        return jsonify({'error': 'Credenciales incorrectas'}), 401
