#crear clase sencilla en python
class MotorElectrico :
    potencia = None

    def encender(self) : 
        print("motor encendido")

    def __init__(self) :
        pass



motor = MotorElectrico()
motor.potencia = 4000
motor.encender()
print(motor.potencia)
