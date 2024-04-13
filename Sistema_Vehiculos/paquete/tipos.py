from pydantic import BaseModel

class Item(BaseModel):
    
    nombre: str
    productos: list[str]
    


class Vehiculo(BaseModel):
    Tipo : str
  
    