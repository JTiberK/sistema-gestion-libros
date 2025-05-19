from models.libro import Libro
from models.inventario import Inventario

# ✅ Libro válido
libro1 = Libro("1984", "George Orwell", 15.5)

# ❌ Libro con precio negativo (debe fallar)
try:
    libro2 = Libro("ErrorBook", "AutorX", -10)
except ValueError as e:
    print(f"🚫 Error esperado: {e}")

# Inventario y operaciones
inventario = Inventario()
inventario.agregar_libro(libro1)

# Agregar más libros
inventario.agregar_libro(Libro("Dune", "Frank Herbert", 20))
inventario.agregar_libro(Libro("Neuromancer", "William Gibson", 18))

# Buscar libro existente
libro_buscado = inventario.buscar_libro("Dune")
print(f"🔍 Encontrado: {libro_buscado}")

# Registrar venta
inventario.registrar_venta("Dune", 2)

# Listar todos
print("📚 Inventario actual:")
for libro in inventario.listar_libros():
    print(f" - {libro}")
