class Nodo :
    def __init__(self , data) :
        self.data = data
        self.id_apuntador = None 
    
class Pila : 
   
        
    def __init__(self) :
        self.cima = None
    
    def almacenar (self , data) :
       nodo = Nodo(data)     
       if self.cima == None:
          self.cima = nodo
          return
       nodo.id_apuntador = self.cima
       self.cima = nodo
       
    def remover (self) :
        if self.cima == None :
            return None
        dato = 
         self.cima = self.id_apuntador 
         return
           
            

    
pila = Pila ()

pila.almacenar(4)
pila.almacenar(3)
pila.almacenar(2)
pila.almacenar(1)


print(pila)

    