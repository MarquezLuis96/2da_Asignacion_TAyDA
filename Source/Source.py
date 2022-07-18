#IMPORTANDO LIBRERIAS
import matplotlib.pyplot as plt

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
    
    #get_dominio - Retorna el dominio de la recta (Xa, Xb) en forma de lista (lista de enteros)
    def get_dominio(self):
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

#Clase Plano - Gestiona el plano X+ e Y+
class Plano:
    lista_rectas:Recta = []
    recta_segmento_de_corte:int = []

    #Constructor
    #constructor - Constructor de la clase Plano
    def __init__(self):
        pass

    #Destructor
    #Destructor - Destructor de la clase Plano
    def __del__(self):
        pass

    #Setters
    #Set_lista_rectas
    def set_lista_rectas(self, lista:Recta):
        self.lista_rectas = lista
    
    #Getters
    #Get_lista_rectas
    def get_lista_rectas(self):
        return self.lista_rectas
    
    #Agregar_recta - agrega una recta a la lista
    def agregar_recta(self, recta:Recta):
        self.lista_rectas.append(recta)
    
    #contar_inter_con_x() - Retorna el numero de intersecciones con la coordenada x que reciba
    def contar_inter_con_x(self, coord_x:int):
        #Coordenadas
        #punto(a/b)coordenada(x/y)
        pacx:int
        pbcx:int

        #contador de intersecciones
        contador_inter:int = 0
        
        #Con este ciclo selecciono cada una de las rectas para verificar si cortan con x
        for i in range(0, self.lista_rectas.__len__()):
            #Se toma el rango de cada recta
            pacx = self.lista_rectas[i].get_punto_A().get_X()
            pbcx = self.lista_rectas[i].get_punto_B().get_X()

            #se pregunta si corta con el dominio
            if(coord_x >= pacx and coord_x <= pbcx):
                #corta con el dominio de la recta
                contador_inter += 1
            else:
                #no corta con el dominio de la recta
                pass
        return contador_inter
    
    #coord_x_mayor_n_cortes - Retorna la coordenada x con el mayor numero de cortes
    #con las rectas pertenecientes al plano
    def coord_x_mayor_n_cortes(self):
        #Mayor numero de cortes
        coord_mas_cortes:int = 0
        mayor_n_cortes:int = 0
        for i in range(0, 10):
            n_cortes_con_i = self.contar_inter_con_x(i)
            if(mayor_n_cortes < n_cortes_con_i):
                coord_mas_cortes = i
                mayor_n_cortes = n_cortes_con_i
        return coord_mas_cortes
    
    #rango_de_x - Retorna el rango (todos los cortes con y) de la linea que realizo los cortes en una lista
    def rango_de_x(self, coord_x:int):
        #Coordenadas
        #punto(a/b)coordenada(x/y)
        pacx:int
        pacy:int
        pbcx:int
        pbcy:int
        
        #Cortes con Y
        cortes_con_y:int = []

        #Con este ciclo selecciono cada una de las rectas para verificar si cortan con x
        for i in range(0, self.lista_rectas.__len__()):
            #Se toma el rango de cada recta
            pacx = self.lista_rectas[i].get_punto_A().get_X()
            pbcx = self.lista_rectas[i].get_punto_B().get_X()

            #se pregunta si corta con el dominio
            if(coord_x >= pacx and coord_x <= pbcx):
                #corta con el dominio de la recta
                #Guarda los valores de Y en los auxiliares
                pacy = self.lista_rectas[i].get_punto_A().get_Y()
                pbcy = self.lista_rectas[i].get_punto_B().get_Y()
                #Guarda los valores de Y en la lista
                cortes_con_y.append(pacy)
                cortes_con_y.append(pbcy)
            else:
                #no corta con el dominio de la recta
                pass

        #Se ordenan los elementos de la lista en forma ascendente
        cortes_con_y.sort()
        return cortes_con_y
    
    #obtener_segmento_de_corte - Obtiene el segmento de corte y todas las coordenadas de corte
    def obtener_segmento_de_corte(self):
        segmento_de_corte:int = 0
        lista_cortes_y:int = []
        n_cortes_y:int = 0

        segmento_de_corte = self.coord_x_mayor_n_cortes()
        lista_cortes_y = self.rango_de_x(segmento_de_corte)
        n_cortes_y = lista_cortes_y.__len__()

        print("El segmento de corte es\nX = " + str(segmento_de_corte))
        print("Ya = " + str(lista_cortes_y[0]))
        print("Yb = " + str(lista_cortes_y[(n_cortes_y - 1)]))
        print("Teniendo un total de " + str(n_cortes_y) + "\n")
        print("Cortes obtenidos:")

        #Guardando en el atributo segmento de corte
        self.recta_segmento_de_corte.append(segmento_de_corte)
        self.recta_segmento_de_corte.append(lista_cortes_y[0])
        self.recta_segmento_de_corte.append(lista_cortes_y[n_cortes_y - 1])

        for i in range(0, lista_cortes_y.__len__()):
            print(str(i+1) + ") x = " + str(segmento_de_corte) + "; y = " + str(lista_cortes_y[i]))
        
        #Escribiendo en el archivo output
        mensaje:str = (str(segmento_de_corte) + " " + str(lista_cortes_y[0]) + " " +
        str(segmento_de_corte) + " " + str(lista_cortes_y[(n_cortes_y - 1)]))

        data_output:Gestor_Archivo = Gestor_Archivo("output.txt")
        data_output.write_to_file(mensaje)
    
    #list_coords - Devuelve una lista de enteros con las coordenadas x o y segun reciba el parametro caracter
    def list_coords(self, coord_to_return:chr):
        lista_coordenadas:int = []
        if coord_to_return == 'x' or coord_to_return == 'X':
            for i in range(0, self.lista_rectas.__len__()):
                lista_coordenadas.append(self.lista_rectas[i].get_punto_A().get_X())
                lista_coordenadas.append(self.lista_rectas[i].get_punto_B().get_X())
        elif coord_to_return == 'y' or coord_to_return == 'Y':
            for i in range(0, self.lista_rectas.__len__()):
                lista_coordenadas.append(self.lista_rectas[i].get_punto_A().get_Y())
                lista_coordenadas.append(self.lista_rectas[i].get_punto_B().get_Y())
        return lista_coordenadas

    def plotear_plano(self):
        #Lista de puntos a plotear
        lista_puntos_x:int = []
        lista_puntos_y:int = []

        #Puntos auxiliares
        xs:int = []
        ys:int = []

        #Llenando las listas de puntos
        lista_puntos_x = self.list_coords('x')
        lista_puntos_y = self.list_coords('y')

        #Ploteando los puntos de entrada
        for i in range(0, lista_puntos_x.__len__(), 2):
            xs = [lista_puntos_x[i], lista_puntos_x[i+1]]
            ys = [lista_puntos_y[i], lista_puntos_y[i+1]]
            plt.plot(xs,ys)
        
        #Ploteando la recta segmento de corte
        xs = [self.recta_segmento_de_corte[0], self.recta_segmento_de_corte[0]]
        ys = [self.recta_segmento_de_corte[1], self.recta_segmento_de_corte[2]]
        plt.plot(xs,ys, "ob--", mfc="r", mec="b")

        #Definiendo máximos y mínimos de los ejes
        max_x:int = max(lista_puntos_x)
        max_y:int = max(lista_puntos_y)
        plt.plot(max_x,max_y)

        #Definiendo etiquetas
        plt.title("Plano")
        plt.xlabel("X")
        plt.ylabel("Y")

        #Mostrando
        plt.show()

#FUNCION RUN - SE ESTABLECE LA SECUENCIA DEL PROGRAMA
def run():
    #DECLARACIONES----------------------------------------------
    #Archivos a manejar
    data_input:Gestor_Archivo = Gestor_Archivo("datos.txt")

    #lista con las rectas leidas de input
    lista_rectas_input:Recta = []

    #Plano X+Y+
    planoxy:Plano = Plano()

    #OPERACIONES----------------------------------------------
    #Se lee los datos y se transforman en una lista
    lista_rectas_input = data_input.read_from_file()

    #Se pasa la lista obtenida al plano x y
    planoxy.set_lista_rectas(lista_rectas_input)

    #Obtener el segmento de corte
    planoxy.obtener_segmento_de_corte()

    #Plotear plano
    planoxy.plotear_plano()

#FUNCION PRINCIPAL - MAIN FUNCTION
if __name__ == "__main__":
    run()