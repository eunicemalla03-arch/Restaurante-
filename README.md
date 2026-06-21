# Sistema de Gestión de Restaurante

## Eunice Belen Malla Coro



## Descripción del proyecto

Este proyecto consiste en un sistema básico de gestión de restaurante desarrollado en Python utilizando Programación Orientada a Objetos (POO). El sistema permite registrar productos y clientes, así como mostrar la información almacenada mediante una estructura modular organizada en carpetas y archivos independientes.

## Estructura del proyecto

restaurante_app/
├── modelos/
│   ├── cliente.py
│   └── producto.py
├── servicios/
│   └── restaurante.py
└── main.py

README.md

### Función de cada archivo

* producto.py: contiene la clase Producto.
* cliente.py: contiene la clase Cliente.
* restaurante.py: contiene la clase Restaurante encargada de administrar los registros.
* main.py: archivo principal donde se crean los objetos y se ejecuta el programa.

## Conceptos aplicados

* Clases y objetos.
* Constructores (**init**).
* Encapsulación básica mediante atributos y métodos.
* Método especial **str**().
* Importación de módulos.
* Organización modular del software.

## Reflexión

La modularización permite dividir un programa en partes más pequeñas y organizadas. Esto facilita el mantenimiento, la reutilación del código y la comprensión del sistema. Separar los modelos, servicios y la ejecución principal ayuda a que cada archivo tenga una responsabilidad específica, mejorando la calidad del software.
