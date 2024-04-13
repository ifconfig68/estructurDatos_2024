from .tipos import Item
from .tipos import Vehiculo

class Nodo:
    def __init__(self, valor: Vehiculo):
        self.valor = valor
        self.siguiente = None
        
       
class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    
    def esta_vacia(self):
        return self.primero is None

    def encolar(self, valor: Vehiculo) :
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
        self.ultimo = nuevo_nodo
    
    def desencolar(self):
        if self.esta_vacia():
            return None
        valor = self.primero.valor
        self.primero = self.primero.siguiente
        if self.primero is None:
            self.ultimo = None
        return valor
    
    def ver_listado(self):
        if self.esta_vacia():
            print("La cola está vacía.")
            return
        current = self.primero
        while current:
            print(current.valor)
            current = current.siguiente
    
    def ver_primero(self):
        if self.esta_vacia():
            return print(f"ingrese datos. la cola se encuentra vacia")
        return self.primero.valor

    def ver_ultimo(self):
        if self.esta_vacia():
            return print(f"ingrese datos. la cola se encuentra vacia")
        return self.ultimo.valor

    def contar(self):
        count = 0
        current = self.primero
        while current:
            count += 1
            current = current.siguiente
        return count