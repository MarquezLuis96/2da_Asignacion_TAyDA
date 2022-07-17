# CLASE PUNTO - UN PUNTO SE DEFINE COMO LA INTERSECCION DE DOS COORDENADAS X E Y
class Punto:

    #Atributos de la clase Punto
    #__x: int = None
    #__y: int = None

    #Constructor
    #Constructor - Recibe parámetros x e y si no asigna None a ambas coordenadas
    def __init__(self,coord_x:int = None, coord_y:int = None):
        self.__x = coord_x
        self.__y = coord_y
    
    #Destructor
    #Destructor del objeto Punto
    def __del__(self):
        pass

    #Setters
    #Set_X - Establece el valor para X
    def set_X(self, coord_x:int):
        self.__x = coord_x
    
    #Set_Y - Establece el valor para Y
    def set_Y(self, coord_Y:int):
        self.__y = coord_Y
    
    #Getters
    #Get_X - Retorna el valor para X
    def get_X(self):
        return self.__x
    
    #Get_Y - Retorna el valor para Y
    def get_Y(self):
        return self.__y
    
    #To_String - Retorna los valores del punto como String
    def to_String(self):
        ret_String = ("(x:" + str(self.__x) + " ; y:" + str(self.__y) + ")")
        return ret_String

#Clase Recta - Una recta se encuentra conformada por dos puntos
class Recta:

    punto_A: Punto = Punto()
    punto_B: Punto = Punto()

    #Constructor
    #Constructor - Recibe como parámetros  dos puntos y si no asigna 0 a ambos puntos
    def __init__(self, punto_Ini:Punto = Punto(), punto_Fin:Punto = Punto()):
        self.punto_A = punto_Ini
        self.punto_B = punto_Fin
    
    #Destructor
    #Destructor del objeto Recta
    def __del__(self):
        pass

    #Setters
    #Set_Punto_A
    def set_Punto_A(self, punto_Ini:Punto):
        self.punto_A = punto_Ini
    
    #Set_Punto_B
    def set_Punto_B(self, punto_Fin:Punto):
        self.punto_B = punto_Fin

    #Getters
    #Get_Punto_A
    def get_punto_A(self):
        return self.punto_A

    #Get_Punto_B
    def get_punto_B(self):
        return self.punto_B
    
    #get_range - Retorna el rango de la recta (Xa, Xb) en forma de lista (lista de enteros)
    def get_range(self):
        #Se crea el objeto rango_recta para retornar el rango de la recta
        rango_recta:int = []
        
        #Se agregan los puntos a la recta
        rango_recta.append(self.punto_A.get_X())
        rango_recta.append(self.punto_B.get_X())

        #Retorna el valor
        return rango_recta


    #To_String - Retorna el punto inicial y final de la recta como un string
    def to_String(self):
        ret_String = ("Punto Inicial: " + self.punto_A.to_String() + " Punto Final: " + self.punto_B.to_String())
        return ret_String

#Clase Gestor_Archivo - permite gestionar los archivos para entradas y salidas de datos mediante archivos .txt
class Gestor_Archivo:
    nombre_Archivo = "my_file.txt"

    #Constructor
    #Constructor - Recibe como parametro el nombre del archivo, si no le asigna el nombre "output.txt"
    def __init__(self, file_name = "output.txt"):
        self.nombre_Archivo = file_name
    
    #Destructor
    #Destructor - Destructor del objeto archivo
    def __del__(self):
        pass

    #Setters
    #Set_file_name - Establece el nombre del archivo a manejar
    def set_file_name(self, file_name):
        self.nombre_Archivo = file_name

    #Getters
    #Get_file_name - Obtiene el nombre del archivo que se maneja
    def get_file_name(self):
        return self.nombre_Archivo
    
    #Rectify - Recibe un string y devuelve una recta con los valores que le son enviados
    def rectify(self, line_readed:str):
        coordenada_int:int = 0
        new_recta:Recta
        puntoA:Punto = Punto()
        puntoB:Punto = Punto()
        for a in range(0, line_readed.__len__()):
            if(line_readed[a].isdigit()):
                if(line_readed[a] == '0'):
                    coordenada_int *= 10
                else:
                    coordenada_int = ((coordenada_int * 10) + (int(line_readed[a])))
            else:
                if puntoA.get_X() == None:
                    puntoA.set_X(coordenada_int)
                elif puntoA.get_Y() == None:
                    puntoA.set_Y(coordenada_int)
                elif puntoB.get_X() == None:
                    puntoB.set_X(coordenada_int)
                elif puntoB.get_Y() == None:
                    puntoB.set_Y(coordenada_int)
                
                coordenada_int = 0

        new_recta = Recta(puntoA, puntoB)
        return new_recta

    #Read_from_file - Lee los datos de un archivo y los transforma a una lista de rectas, lista la cual se retorna
    def read_from_file(self):
        #n_rectas - almacena el numero de rectas a leer y por consiguiente n ciclos a realizar
        n_rectas:int = 0

        #line_readed - almacena la linea leida del archivo
        line_readed:str = ""

        #Lista a retornar - retorna la lista de las rectas a graficar
        ret_list:Recta = []

        #Abriendo el archivo
        file = open(self.nombre_Archivo, "r")

        #Leyendo el numero de rectas a almacenar
        n_rectas = int(file.readline())

        #Recorriendo todas las líneas del archivo
        for index_linea in range(0, n_rectas):
            
            #leyendo una linea
            line_readed = file.readline()

            #convirtiendo el string obtenido en una recta
            newRecta = self.rectify(line_readed)

            #Guardando dicha recta en una lista
            ret_list.append(newRecta)
        
        #Cerrando archivo
        file.close()

        #Lineas utilizadas para ver los datos cargados en la lista
        # for index_linea in range(0, ret_list.__len__()):
        #     print(ret_list[index_linea].to_String())

        #Se retorna la lista
        return ret_list

    #Write_result_to_file - Escribe el resultado en el archivo de texto cuyo nombre es nombre_Archivo
    def write_to_file(self, mensaje:str):
        file = open(self.nombre_Archivo, "w")
        file.write(mensaje)
        file.close()


#FUNCION RUN - SE ESTABLECE LA SECUENCIA DEL PROGRAMA
def run():
    lista_de_rectas:Recta = []
    lista_de_rangos = []

    print("leyendo...")
    archivo_a_leer = Gestor_Archivo("datos.txt")
    lista_de_rectas = archivo_a_leer.read_from_file()

    print("ecribiendo...")
    archivo_a_escribir = Gestor_Archivo()
    archivo_a_escribir.write_to_file("Esta es una linea de prueba")

    for i in range(0, lista_de_rectas.__len__()):
        lista_de_rangos.append(lista_de_rectas[i].get_range())
    
    for i in range(0, lista_de_rangos.__len__()):
        aux:int = 0
        print("Rango recta " + str(i+1) + ": ")

        aux = lista_de_rangos[i][0]
        print("XA: " + str(aux))

        aux = lista_de_rangos[i][1]
        print("XB: " + str(aux))

#FUNCION PRINCIPAL - MAIN FUNCTION
if __name__ == "__main__":
    run()