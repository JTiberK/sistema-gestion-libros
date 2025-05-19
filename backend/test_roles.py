from models.usuario import Usuario, Moderador, Admin, login

print("🔐 Test de roles")

# Usuario normal
user = Usuario("juan", "1234")
print("👤 Usuario:", login(user, "1234"))           # ✅ True
print("👤 Usuario (mal):", login(user, "wrong"))     # ❌ False

# Moderador
mod = Moderador("mod1", "mod_abc")
print("🛡️ Moderador:", login(mod, "mod_abc"))       # ✅ True
print("🛡️ Moderador (sin prefix):", login(mod, "abc"))  # ❌ False

# Admin
admin = Admin("admin1", "mi@clave")
print("⚙️ Admin:", login(admin, "mi@clave"))         # ✅ True
print("⚙️ Admin (sin char especial):", login(admin, "miclave"))  # ❌ False
