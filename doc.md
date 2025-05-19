# Comprobar si Python está instalado

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
<br>
<br>
<br>

# Documentation (⛏️ Flask Basic Start)

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