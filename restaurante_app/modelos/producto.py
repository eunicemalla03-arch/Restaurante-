# Clase Producto: representa un plato, bebida o postre del restaurante

class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def __str__(self):
        return f"{self.nombre} ({self.categoria}) - ${self.precio:.2f}"

    def mostrar_info(self):
        print(f"Producto: {self.nombre}, Categoría: {self.categoria}, Precio: ${self.precio:.2f}")
