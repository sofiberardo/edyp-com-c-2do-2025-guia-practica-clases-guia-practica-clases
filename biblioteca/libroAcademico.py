from libro import Libro

#libro academico hereda de libro todos los atributos y metodos pero agrego
# materia, nivel educativo y laboratorio


class LibroAcademico(Libro):
    #constructor
    niveles_validos=['primaria','secundaria','universidad','posgrado']
    def __init__(self,titulo:str,autor:str,editorial:str,ISBN:str,materia:str,nivel:str,estado='disponible',requiere_laboratorio=False):
        super().__init__(titulo,autor,editorial,ISBN,estado)
        #usando
        #Libro.__init__(self,....)
        self.materia=self.validar_cadena(materia)
        self.nivel=nivel
        self.requiere_laboratorio=self.requieres_laboratorio(requiere_laboratorio)
    
    def requieres_laboratorio(self,requiere_laboratorio:bool):
        if not isinstance(requiere_laboratorio,bool):
            raise TypeError ('El tipo de dato debe ser un bool')
        return requiere_laboratorio
    
    # def __str__(self):
        # frase_saludo=super().__str__()
        # if self.requiere_laboratorio==True:
        #     laboratorio='Requiere Laboratorio'
        # else:
        #     laboratorio='No Requiere Laboratorio'
        # return f'{frase_saludo}. Es un libro de {self.materia} del nivel {self.nivel} y {laboratorio}'
    
if __name__=='__main__':
    try:
        fisica=LibroAcademico('fisica 1','No me molestes','sufrir','12345','Fisica','universitario',requiere_laboratorio=True)
        print(fisica)
        print(LibroAcademico.__mro__)
            
    except TypeError as e:
            print('El error es:',e)
    except ValueError as e:
            print('El error es:',e)
    except Exception as e:
            print('El error es:',e)