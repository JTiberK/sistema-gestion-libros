from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

# Rutas
from routes.libros import libros_bp
from routes.auth import auth_bp
app.register_blueprint(libros_bp)
app.register_blueprint(auth_bp)

@app.route('/')
def home():
    return 'API OK ✅'

# Inicializar DB
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
