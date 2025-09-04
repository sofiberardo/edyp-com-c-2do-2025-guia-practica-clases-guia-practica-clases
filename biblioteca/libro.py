class Libro:
    # constructor
    posibles_estados=['disponible','prestado'] # atributo de clase
    contador_libros=0 # atributo de clase

    
    def __init__(self,titulo:str,autor:str,editorial:str,ISBN:str,estado='disponible'):
        self.titulo=self.validar_cadena(titulo)# atributos de instancia
        self.autor=self.validar_cadena(autor)
        self.editorial=self.validar_cadena(editorial)
        self.ISBN=ISBN
        self.estado=self.setter_estado(estado)
        Libro.contador_libros+=1
        
    @classmethod
    def mostrar_contador_libros(cls):
        print(f'El numero de libros creados es: {cls.contador_libros}')
    
        
    #visualizar la información de cada libro
    # def __str__(self):
    #     return f' El libro {self.titulo} es del autor {self.autor} y la editorial es {self.editorial } con ISBN{self.ISBN}, y su estado es {self.estado}'
    
    def mostrar(self):
        return f' El libro {self.titulo} es del autor {self.autor} y la editorial es {self.editorial } con ISBN{self.ISBN}, y su estado es {self.estado}'

    def getter_estado(self):
        return self.estado
    
    def getter_ISBN(self):# no se ha validado, puede construir un objeto libro incorrecto al pasar un ISBN no valido
        return self.ISBN
    
    def devolver_libro(self):
        if self.estado=='disponible':
            print('El libro ya se encuentra disponible')
        else:
            self.setter_estado('disponible')
            print('El libro ha sido devuelto y se encuentra disponible')
    
    def prestar_libro(self):
        if self.getter_estado()=='disponible':
            self.estado='prestado'
            print(f'El libro {self.titulo} fue prestado con exito')
        else:
            print(f' El libro {self.titulo} no se encuentra disponible para prestar')
    
    def validar_cadena(self,cadena:str):
        if not isinstance(cadena,str):
            raise TypeError('El titulo debe ser una cadena de texto')
        if len(cadena)==0:
            raise ValueError('El titulo no puede estar vacio')
        return cadena
 
    def setter_estado(self,estado):
        estado=estado.lower()
        if estado not in Libro.posibles_estados:
            raise ValueError(f'El estado debe ser uno de los siguientes: {self.posibles_estados}')
        self.estado=estado
        return estado
    
    def __eq__(self,otro):
        if not isinstance(otro,Libro):
            raise TypeError('El objeto debe ser una instancia de la clase Libro')
        elif id(self)==id(otro):
            return True
        elif self.ISBN==otro.ISBN:
            return True
        else:
            return False
        

# prueba de la clase
if __name__=='__main__':
    try:
            carlos=Libro('Cien años de soledad','Gabriel Garcia Marquez','Sudamericana','1234567890')
            print(carlos)
            print(carlos.mostrar())
            carlos.setter_estado('prestado')
            print(carlos.getter_estado())
            carlos1=Libro('Cien años de soledad','Gabriel Garcia Marquez','Sudamericana','1234567891')
            print(Libro.contador_libros)
            print(carlos1)
            carlos2=Libro('Cien años de soledad','Gabriel Garcia Marquez','Sudamericana','1234567890')
            print(carlos==carlos2)
            print(carlos==carlos1)
    except TypeError as e:
            print('El error es:',e)
    except ValueError as e:
            print('El error es:',e)
    except Exception as e:
            print('El error es:',e)
        
        