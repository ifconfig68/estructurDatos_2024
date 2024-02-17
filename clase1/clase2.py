##crear clase padre 



class Articulo :
    count_obj =0 

    def __init__(self,  name, price):
        self.nombre = name
        self.precio = price
        Articulo.count_obj0 +=1
        print(f"obejeto {Articulo.count_obj} creado")

       
