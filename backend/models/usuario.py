# backend/models/usuario.py

import re

class Usuario:
    def __init__(self, username: str, password: str):
        self.username = username
        self._password = password

    def autenticar(self, pwd: str) -> bool:
        return self._password == pwd

class Moderador(Usuario):
    def autenticar(self, pwd: str) -> bool:
        if not pwd.startswith("mod_"):
            return False
        return super().autenticar(pwd)

class Admin(Usuario):
    def autenticar(self, pwd: str) -> bool:
        if not re.search(r"[!@#$%^&*()_+]", pwd):
            return False
        return super().autenticar(pwd)

# Función polimórfica
def login(usuario: Usuario, pwd: str) -> bool:
    return usuario.autenticar(pwd)
