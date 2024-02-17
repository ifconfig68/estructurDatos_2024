##crear clase padre 



class Articulo :
    
    tipo: str
    anio:int
    referencia:str
    contador = 0

    def __init__(self,  name, price):
     self.nombre = name
     self.precio = price
     Articulo.contador =+ 1


    def asignar_tipo (self , tipo):
        self.tipo = tipo
           
    def asignar_anio(self ,  anio) -> None :
        self.anio = anio

    def asignar_referecia (self , referencia) -> None: 
       self.referencia = referencia

    def obtener_nombre(self ) -> str : 
       return self.nombre

    def obtener_tipo (self) -> str :
       return self.tipo
    
    def obtener_precio (self) -> int :
       return self.precio
    
    def obtener_anio (self) -> int :
       return self.anio
    
    def obrtener_referencia (self) -> int :
       return self.referencia
    
@staticmethod
def procesar () : 
    pass



class Pantalla (Articulo) :
   
   resolucion = str
   alto = int 
   ancho = int
   tasa_refresco = int


   def __init__(self, name, price):
      super().__init__(name, price)
      self.tipo = "Pantalla"


def asignar_resolucion (self , resolucion) ->None: 
    self.resolucion = resolucion

def asignar_alto (self , alto)->None : 
   self.alto = alto

def asignar_ancho(self  , ancho)-> None :
   self.ancho = ancho

def asignar_tasa_refresco(self , tasa_refresco) -> None :
   self.tasa_refresco = tasa_refresco 


def obetener_resolucion (self) ->str: 
    return self.resolucion

def obetener_alto (self ) ->int: 
    return self.alto

def obetener_ancho (self ) ->int: 
    return self.alto

def asignar_tasa_refresco(self) -> int :
   return self.tasa_refresco 



pantalla = Articulo("dell " , 3)
pantalla2 = Articulo("dell2  " , 3)
print(f"hola {pantalla.nombre} objeto {Articulo.contador} creado")
print(f"hola {pantalla2.nombre} objeto {Articulo.contador} creado")



pantalla



        
       
