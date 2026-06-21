# Clase Restaurante: administra productos y clientes

class Restaurante:
    def __init__(self):
        self.productos = []
        self.clientes = []

    def registrar_producto(self, producto):
        self.productos.append(producto)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_productos(self):
        print("\n--- Productos disponibles ---")
        if not self.productos:
            print("No hay productos registrados.")
        else:
            for producto in self.productos:
                print(producto)

    def mostrar_clientes(self):
        print("\n--- Clientes registrados ---")
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in self.clientes:
                print(cliente)
