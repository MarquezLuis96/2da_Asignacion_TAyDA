# CLASE PUNTO - UN PUNTO SE DEFINE COMO LA INTERSECCION DE DOS COORDENADAS X E Y
from re import X


class Punto:

    #Atributos de la clase Punto
    x = 0
    y = 0

    #Constructor
    #Constructor - recibe parámetros x e y si no asigna 0 a ambas coordenadas
    def __init__(self,coord_x = 0, coord_y = 0):
        self.x = coord_x
        self.y = coord_y
    
    #Destructores
    #Destructor del objeto punto
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

##

#FUNCION RUN - SE ESTABLECE LA SECUENCIA DEL PROGRAMA
def run():
    punto1 = Punto()
    punto2 = Punto(10, 20)

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



#FUNCION PRINCIPAL - MAIN FUNCTION
if __name__ == "__main__":
    run()