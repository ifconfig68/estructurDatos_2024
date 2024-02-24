class Vehiculo :
    def __init__(self ,marca , conbustible  ):
        self.marca = marca
        self.conbustible = conbustible

    def ver_autos(self) :
        print (f"auto {self.marca} - conbustible {self.conbustible}")

    def encender () :
        print ("motor encendido")

    def arrancar () :
        print ("motor encendido")


def __str__  (self) :
     return f"Auto {self.marca} - combustuble{self.conbustible}"


class Motos(Vehiculo) :
    def __init__(self, marca, conbustible):
        super().__init__(marca, conbustible)
    

    



if __name__ == "__main__" :
    pass 
    autos = []
    for j in range (10) :
        n = input ("ingrese Marca de auto ")
        c = input ("ingrese tipo de conbustible ")
        autos.append(Vehiculo(n , c))

    for i in autos :
        print (i)


    autos[0].ver_autos()
    autos[1].ver_autos()
    autos[2].ver_autos()
    autos[3].ver_autos()


    

