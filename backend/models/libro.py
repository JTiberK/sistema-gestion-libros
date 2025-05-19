# backend/models/libro.py

class Libro:
    def __init__(self, titulo: str, autor: str, precio: float):
        self.__titulo = titulo
        self.__autor = autor
        self.precio = precio  # usa setter con validación

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError('Precio negativo')
        self.__precio = valor

    def __str__(self):
        return f'"{self.__titulo}" de {self.__autor} - ${self.__precio:.2f}'
