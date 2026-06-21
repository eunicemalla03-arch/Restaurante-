# Clase Cliente: representa a un cliente del restaurante

class Cliente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.pedidos = []  # lista de productos pedidos

    def __str__(self):
        return f"Cliente: {self.nombre}, Edad: {self.edad}"

    def agregar_pedido(self, producto):
        self.pedidos.append(producto)

    def mostrar_pedidos(self):
        print(f"\nPedidos de {self.nombre}:")
        if not self.pedidos:
            print(" - No tiene pedidos registrados.")
        else:
            for producto in self.pedidos:
                print(f" - {producto}")
