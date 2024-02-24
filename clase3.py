def  multiplicacion (a : int ,  b : int ) -> int :
    if a == 1 :
        return b
    return b + multiplicacion(a-1,b)
 
print (multiplicacion(5 , 2))


#hacer division utilizando restas

