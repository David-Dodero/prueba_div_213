def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos: int)->int|None:

    while reintentos > 0:
        numero= int(input(mensaje))
        if numero >= minimo and numero <= maximo:
            return numero        
        else:
            numero=int(input(mensaje_error))            
            reintentos -= 1
    return None
# resultado=get_int("ingrese un numero entero: ", "errorazo ingrese un numero entero: ", 1, 10, 5)

# print("el resultado es",resultado)            

def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos: float)->float|None:

    while reintentos > 0:
        numero= float(input(mensaje))
        if numero >= minimo and numero <= maximo:
            return numero        
        else:
            numero=float(input(mensaje_error))            
            reintentos -= 1
    return None


def get_string(longitud: int)-> str|None:
    while True:
        cadena = input(f"Ingrese una cadena de longitud {longitud}: ")
        if len(cadena) == longitud:
            return cadena  # Retorna la cadena válida
        else:
            print(f"Error: la cadena debe tener exactamente {longitud} caracteres. Inténtelo de nuevo.")

# resultado = get_string(5)  # Por ejemplo, se espera una cadena de longitud 5
# print("Cadena ingresada:", resultado)