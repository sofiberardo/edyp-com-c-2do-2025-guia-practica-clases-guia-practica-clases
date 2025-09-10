# Ejercicio 2: Modelar una computadora
# 
# En este archivo debés crear la clase Computadora siguiendo las consignas del README.
# Recordá:
# - Definir atributos relevantes en el constructor (__init__), con valores por defecto.
# - Implementar el método __str__ para mostrar la información esencial.
# - Instanciar al menos 3 computadoras con distintos valores.
# - Llevar la cuenta de computadoras creadas (usar variable de clase).
# - Implementar al menos 2 métodos de los sugeridos (updateOS, PM, addRAM, getCapacity).
# - Crear otra clase para un componente (ej: Disco, RAM, etc.) con su propio __init__, __str__ y al menos un método.
# 
# ¡No olvides probar todos los métodos y comentar tu criterio para los valores

# README
# En este ejercicio vamos a modelar una computadora, creando la clase `Computadora` para ello.
# Primero, pensá un rato en todas las características que mirarías al momento de comprar una. ¿Cómo llamamos a esas características en el paradigma de la programación orientada a objetos? Atributos
# Luego de pensarlo, continuá con la consigna.
# - El objeto computadora debe ser instanciado con todos sus atributos pasados como parámetros al método constructor. Al momento de crear el equipo, asignales a los atributos valores por defecto. ¿Qué criterio tuviste en cuenta para elegir esos valores?
# - El método `__str__` nos ayuda a conocer la información esencial de nuestros objetos. ¡Implementalo! Recordá que siempre debería estar presente en las clases que creás.
# - Instanciá 3 computadoras y asignales distintos valores a sus atributos.
# - ¿Cómo podrías llevar la cuenta de la cantidad de computadoras creadas? ¿Qué tipo de variable resuelve lo pedido? Método de clase

# - Implementá al menos 2 de los siguientes métodos en la clase Computadora:
#   - `updateOS`: Actualiza el sistema operativo.
#   - `PM`: Brinda un mantenimiento programado al hardware del equipo.
#   - `addRAM`: Instala un nuevo módulo de RAM en la computadora.
#   - `getCapacity`: Muestra la capacidad del componente de hardware que se desee conocer.

# > Nota: Pedile ayuda a tu monitor para pensar cómo implementar los métodos solicitados. Pensá en aquellos atributos creados u otros adicionales que les den funcionalidad y practicidad a dichos métodos. Si es necesario, podés investigar el uso de `datetime` u otra librería que requieras. Recordá informar siempre al usuario sobre las acciones realizadas en el sistema. Probá todos los métodos creados para testear su funcionamiento.
# - Elegí algún componente de hardware o software de la máquina (atributo) y dale identidad. Para ello, creá otra clase, definí el constructor, el `__str__` y pensá en al menos una función que sea aplicable al componente elegido. Codificá el/los métodos pensados. ¿Qué acciones realizan los métodos elegidos sobre los atributos? ¿Una lectura (read)? ¿Una escritura (write)? ¿Una ejecución (exec)?

# Atributos: marca, capacidad, sistema operativo, procesador

class Computadora:
    contador_computadoras = 0
    
    def __init__(self, marca: str, ram: None, sistema_op: str, procesador: str):
        self.marca = marca
        self.ram = ram if ram else RAM()
        self.sistema_op = sistema_op
        self.procesador = procesador
        Computadora.contador_computadoras+=1
    
    def __str__(self):
        return f'Marca: {self.marca}\nCapacidad: {self.capacidad}\nSistema operativo: {self.sistema_op}\nProcesador: {self.procesador}.'
    
    def addRAM(self):
        extra = input('Ingrese la capacidad del nuevo módulo de RAM: ')
        self.ram.upgrade(extra)
        
    def updateOS(self):
        nuevoOS = input('Ingrese el nuevo sistema operativo a instalar: ')
        self.sistema_op = nuevoOS
        print(f'El nuevo sistema operativo: {nuevoOS} ha sido instalado con éxito.')

class RAM:
    def __init__ (self, capacidad=4):
        self.capacidad = capacidad
    
    def __str__(self):
        return f'La RAM es {self.capacidad} GB.'
    
    def __getCap__(self):
        return self.capacidad
    
    def upgrade (self, extra):
        self.capacidad += extra
        print(f'La RAM fue actualizada, ahora tiene {self.capacidad} GB.') 
        