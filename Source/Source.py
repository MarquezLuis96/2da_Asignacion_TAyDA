# CLASE PUNTO - UN PUNTO SE DEFINE COMO LA INTERSECCION DE DOS COORDENADAS X E Y
class Punto:

    #Atributos de la clase Punto
    x = 0
    y = 0

    #Constructor
    #Constructor - Recibe parámetros x e y si no asigna 0 a ambas coordenadas
    def __init__(self,coord_x = 0, coord_y = 0):
        self.x = coord_x
        self.y = coord_y
    
    #Destructor
    #Destructor del objeto Punto
    def __del__(self):
        pass

    #Setters
    #Set_X - Establece el valor para X
    def set_X(self, coord_x):
        self.x = coord_x
    
    #Set_Y - Establece el valor para Y
    def set_Y(self, coord_Y):
        self.y = coord_Y
    
    #Getters
    #Get_X - Retorna el valor para X
    def get_X(self):
        return self.x
    
    #Get_Y - Retorna el valor para Y
    def get_Y(self):
        return self.y
    
    #To_String - Retorna los valores del punto como String
    def to_String(self):
        ret_String = ("(x:" + str(self.x) + " ; y:" + str(self.y) + ")")
        return ret_String

#Clase Recta - Una recta se encuentra conformada por dos puntos
class Recta:

    punto_A = Punto()
    punto_B = Punto()

    #Constructor
    #Constructor - Recibe como parámetros  dos puntos y si no asigna 0 a ambos puntos
    def __init__(self, punto_Ini = Punto(), punto_Fin = Punto()):
        self.punto_A = punto_Ini
        self.punto_B = punto_Fin
    
    #Destructor
    #Destructor del objeto Recta
    def __del__(self):
        pass

    #Setters
    #Set_Punto_A
    def set_Punto_A(self, punto_Ini):
        self.punto_A = punto_Ini
    
    #Set_Punto_B
    def set_Punto_B(self, punto_Fin):
        self.punto_B = punto_Fin

    #Getters
    #Get_Punto_A
    def get_punto_A(self):
        return self.punto_A

    #Get_Punto_B
    def get_punto_B(self):
        return self.punto_B
    
    #To_String - Retorna el punto inicial y final de la recta como un string
    def to_String(self):
        ret_String = ("Punto Inicial: " + self.punto_A.to_String() + " Punto Final: " + self.punto_B.to_String())
        return ret_String

#FUNCION RUN - SE ESTABLECE LA SECUENCIA DEL PROGRAMA
def run():
    punto1 = Punto()
    punto2 = Punto(10, 20)
    recta1 = Recta()

    print("Punto 1:\n")
    print("X = " + str(punto1.get_X()) + " ; Y = " + str(punto1.get_Y()) + "\n")

    print("Punto 2:\n")
    print("X = " + str(punto2.get_X()) + " ; Y = " + str(punto2.get_Y()) + "\n")

    print("\nCambiando valores a punto 1...\n\n")
    punto1.set_X(25)
    punto1.set_Y(60)

    print("Punto 1:\n")
    print("X = " + str(punto1.get_X()) + " ; Y = " + str(punto1.get_Y()) + "\n")

    print("Punto 2:\n")
    print("X = " + str(punto2.get_X()) + " ; Y = " + str(punto2.get_Y()) + "\n")

    print("Recta Vacia:\n" + recta1.to_String() + "\n")
    recta1.set_Punto_A(punto1)
    recta1.set_Punto_B(punto2)
    print("Recta Dibujada:\n" + recta1.to_String() + "\n")



#FUNCION PRINCIPAL - MAIN FUNCTION
if __name__ == "__main__":
    run()