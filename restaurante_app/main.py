# Archivo principal: punto de arranque del programa
# Aquí se crean objetos y se demuestra el funcionamiento del sistema

from modelos.cliente import Cliente
from modelos.producto import Producto
from servicios.restaurante import Restaurante

def main():
    # Crear restaurante
    restaurante = Restaurante()

    # Crear productos
    p1 = Producto("Pizza", 8.5, "Plato fuerte")
    p2 = Producto("Coca-Cola", 1.5, "Bebida")
    p3 = Producto("Helado", 2.0, "Postre")

    # Registrar productos
    restaurante.registrar_producto(p1)
    restaurante.registrar_producto(p2)
    restaurante.registrar_producto(p3)

    # Crear cliente
    c1 = Cliente("Ana", 25)
    c1.agregar_pedido(p1)
    c1.agregar_pedido(p3)

    # Registrar cliente
    restaurante.registrar_cliente(c1)

    # Mostrar información
    restaurante.mostrar_productos()
    restaurante.mostrar_clientes()
    c1.mostrar_pedidos()

if __name__ == "__main__":
    main()
