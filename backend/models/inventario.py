# backend/models/inventario.py

from .libro import Libro

class Inventario:
    def __init__(self):
        self._libros = []
        self._ventas_log = []

    def agregar_libro(self, libro: Libro):
        self._libros.append(libro)

    def buscar_libro(self, titulo: str):
        for libro in self._libros:
            if libro.titulo == titulo:
                return libro
        return None

    def registrar_venta(self, titulo: str, cantidad: int):
        libro = self.buscar_libro(titulo)
        if libro:
            self._ventas_log.append({
                'titulo': titulo,
                'cantidad': cantidad
            })
            print(f'✅ Venta registrada: {cantidad} x {libro.titulo}')
        else:
            raise ValueError('Libro no encontrado')

    def listar_libros(self):
        return [str(libro) for libro in self._libros]
