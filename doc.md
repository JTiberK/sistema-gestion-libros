# Fase 1 - Preparación del entorno

## Comprobar si Python está instalado

Para verificar si tienes Python instalado en tu sistema, sigue estos pasos:

1. Abre una terminal o consola de comandos.
2. Escribe el siguiente comando y presiona Enter:

    ```bash
    python --version
    ```

    O, dependiendo de tu sistema, prueba con:

    ```bash
    python3 --version
    ```

3. Si Python está instalado, verás un mensaje con la versión de Python, como por ejemplo:

    ```
    Python 3.10.7
    ```

4. Si no está instalado, recibirás un mensaje de error indicando que el comando no se reconoce.

5. En caso de no tener Python, puedes descargarlo desde su sitio oficial: [https://www.python.org/](https://www.python.org/).

## Crear y activar un entorno virtual

Para aislar las dependencias de tu proyecto en Windows, sigue estos pasos:

1. Ejecuta el siguiente comando para crear un entorno virtual llamado `venv`:

    ```bash
    python -m venv venv
    ```

2. Activa el entorno virtual con el siguiente comando:

    ```bash
    venv\Scripts\activate
    o
     .\venv\Scripts\activate
    ```

3. Una vez activado, cualquier paquete que instales usando `pip` se instalará únicamente en este entorno, aislando las dependencias de tu proyecto.

## Instalar dependencias del proyecto

Para instalar las dependencias necesarias para este proyecto, ejecuta el siguiente comando:

```bash
pip install Flask Flask-SQLAlchemy flask-cors
```

Esto instalará los paquetes `Flask`, `Flask-SQLAlchemy` y `flask-cors` en tu entorno virtual.

## Crear la estructura del proyecto

Para organizar el proyecto, crea la siguiente estructura de directorios y archivos ejecutando los comandos:

```bash
# En Linux (NO COMPROBADO)
mkdir -p backend/models backend/routes
touch backend/app.py backend/config.py
```


```bash
# En PowerShell  # En Terminal VS Studio
New-Item -Path backend\models -ItemType Directory
New-Item -Path backend\routes -ItemType Directory
New-Item -Path backend\app.py -ItemType File
New-Item -Path backend\config.py -ItemType File
```

Esto creará:

- Un directorio `backend/models` para los modelos de datos.
- Un directorio `backend/routes` para las rutas de la aplicación.
- Un archivo `backend/app.py` que será el punto de entrada de la aplicación.
- Un archivo `backend/config.py` para la configuración del proyecto.

<br>

## Documentation (⛏️ Flask Basic Start)

## Overview
This code initializes a simple Flask web application with Cross-Origin Resource Sharing (CORS) enabled. It defines a single route (`/`) that serves as the home endpoint, returning a confirmation message when accessed.

## Components

### Imports
- **Flask**: A lightweight WSGI web application framework used to create the web server.
- **CORS**: A Flask extension that allows handling Cross-Origin Resource Sharing (CORS), enabling the API to be accessed from different domains.

### Application Initialization
- `app = Flask(__name__)`: Creates an instance of the Flask application.
- `CORS(app)`: Enables CORS for the Flask application, allowing requests from external origins.

### Routes
- `@app.route('/')`: Defines the root endpoint (`/`) of the application.
    - **Function**: `home()`
        - Returns the string `'API OK ✅'` as a response to indicate that the API is running successfully.

### Main Execution
- `if __name__ == '__main__':`: Ensures the application runs only when the script is executed directly.
    - `app.run(debug=True)`: Starts the Flask development server with debugging enabled, allowing for real-time error tracking and automatic reloading during development.

## Usage
1. Run the script to start the Flask server.
2. Access the root endpoint (`http://127.0.0.1:5000/`) in a web browser or API client to verify the API is operational.
3. The response should display: `API OK ✅`.

## Notes
- **CORS**: This setup is useful for APIs that need to be accessed from web applications hosted on different domains.
- **Debug Mode**: The `debug=True` setting is intended for development purposes only and should not be used in production environments.

<br>
<br>
<br>
<br>

# Fase 2 – Clases y Encapsulación

## 📘 Clase Libro (libro.py)
    Privacidad y validaciones:

    __titulo, __autor, __precio como atributos privados.

    Getters y setters con @property.

    Setter precio lanza ValueError si < 0.

## 📚 Clase Inventario (inventario.py)
    Gestión de libros en memoria:

    Lista privada: _libros = []

    agregar_libro(libro) agrega a lista.

    buscar_libro(titulo) busca coincidencia exacta.

    registrar_venta(titulo, cantidad) → simula venta o lanza error si no existe.

## 🧪 ¿Test manual?
    Es un script de prueba temporal, un archivo .py donde simulás acciones reales del sistema:

    Crear libros

    Validar errores

    Agregar al inventario

    Buscar libros

    Registrar ventas

### Ejecución

```bash
cd backend
python test_manual.py

# En VS Code solo hay que pulsar ▶️
```

<br>
<br>
<br>
<br>

# Fase 3 – Sistema de Autenticación

## 🧠 Planificación
    🧑‍💻 Usuario
    username: público

    _password: protegido

    Método autenticar(pwd) → devuelve True si coincide con _password

    🛡️ Moderador(Usuario)
    Requiere que el pwd comience con "mod_" y coincida con _password.

    🛠️ Admin(Usuario)
    Requiere que el pwd contenga un carácter especial como @, #, etc.

    Luego llama a super().autenticar(pwd) para validar base.


## 🛠️ PASOS DETALLADOS

### 🔢 1. Crear la clase base Usuario

    🧱 Archivo: backend/models/usuario.py

```bash
class Usuario:
    def __init__(self, username: str, password: str):
        self.username = username
        self._password = password

    def autenticar(self, pwd: str) -> bool:
        return self._password == pwd
```

    🔍 Esta clase:

    Guarda el nombre y contraseña.

    Usa un método autenticar() que compara la contraseña dada (pwd) con la almacenada (_password).

    Este método es base, y será sobrescrito por subclases.

### 🔢 2. Crear subclase Moderador(Usuario)

```bash
class Moderador(Usuario):
    def autenticar(self, pwd: str) -> bool:
        if not pwd.startswith("mod_"):
            return False
        return super().autenticar(pwd)
```

    🛡️ Reglas para Moderador:

    La contraseña debe empezar con "mod_".

    Luego se compara como lo haría un Usuario común usando super().autenticar(pwd).

### 🔢 3. Crear subclase Admin(Usuario)

```bash
import re

class Admin(Usuario):
    def autenticar(self, pwd: str) -> bool:
        if not re.search(r"[!@#$%^&*()_+]", pwd):
            return False
        return super().autenticar(pwd)
```

    ⚙️ Reglas para Admin:

    La contraseña debe contener al menos un carácter especial (@, #, etc.).

    Luego llama al método base autenticar para verificar que coincida exactamente.

### 🔢 4. Crear la función polimórfica login()

```bash
def login(usuario: Usuario, pwd: str) -> bool:
    return usuario.autenticar(pwd)
```

    🌀 Esto usa polimorfismo:

    Acepta cualquier objeto que herede de Usuario.

    Llama a su método autenticar(), que se comportará diferente según la subclase (Usuario, Moderador, Admin).


### 🔢 5. tests manuales

```bash
cd backend
python test_roles.py

# En VS Code solo hay que pulsar ▶️
```

<br>
<br>
<br>
<br>

# Fase 4 – API REST con Flask + SQLAlchemy

### 🔢 1. Instalar dependencias

```bash
    # Para Instalar
    pip install Flask Flask-SQLAlchemy flask-cors 

    # Para desinstalar
    pip uninstall Flask Flask-SQLAlchemy flask-cors
    ```
```

### 🔢 2. Configurar base de datos
        📄 backend/config.py

```bash
    SQLALCHEMY_DATABASE_URI = 'sqlite:///libros.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    Esto creará libros.db en la raíz de backend.
```

### 🔢 3. Modificar app.py para levantar SQLAlchemy
        📄 backend/app.py

### 🔢 4. Modelo LibroModel + sincronización con clase Libro
        📄 backend/models/libro.py

### 🔢 5. Rutas de Libros – CRUD REST
        📄 backend/routes/libros.py

### 🔢 6. Rutas de Login – roles dinámicos
        📄 backend/routes/auth.py

