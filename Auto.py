class Vehiculo :

def __init__(self ,marca , conbustible ):
        self.marca = marca
        self.conbustible = conbustible

def encender () :
    print ("motor encendido")

def arrancar () :
    print ("motor encendido")

def __str__(self):
    return f"""
        {self.marca}
        {self.conbustible}
        """

auto = Auto("marca x" , "yy")
print (auto)