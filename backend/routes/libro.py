from flask import Blueprint, request, jsonify
from models.libro import LibroModel
from backend.app import db

libros_bp = Blueprint('libros', __name__, url_prefix='/api/libros')

@libros_bp.route('', methods=['GET'])
def obtener_libros():
    libros = LibroModel.query.all()
    return jsonify([l.to_dict() for l in libros])

@libros_bp.route('', methods=['POST'])
def crear_libro():
    data = request.json
    if data['precio'] < 0:
        return jsonify({'error': 'Precio negativo'}), 400
    nuevo = LibroModel(titulo=data['titulo'], autor=data['autor'], precio=data['precio'])
    db.session.add(nuevo)
    db.session.commit()
    return jsonify(nuevo.to_dict()), 201

@libros_bp.route('/<int:id>', methods=['GET'])
def obtener_libro(id):
    libro = LibroModel.query.get_or_404(id)
    return jsonify(libro.to_dict())

@libros_bp.route('/<int:id>', methods=['PUT'])
def actualizar_libro(id):
    libro = LibroModel.query.get_or_404(id)
    data = request.json
    if 'precio' in data:
        if data['precio'] < 0:
            return jsonify({'error': 'Precio negativo'}), 400
        libro.precio = data['precio']
    db.session.commit()
    return jsonify(libro.to_dict())

@libros_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_libro(id):
    libro = LibroModel.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    return jsonify({'mensaje': 'Libro eliminado'})
