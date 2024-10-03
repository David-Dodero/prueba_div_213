#validate_number()
#validate_length()

# def validate_number(mensaje: str,mensaje_error:str, minimo:int, maximo:int):
#     numero= int(input(mensaje))
#         if numero >= minimo and numero <= maximo:
#             return numero        
#         else:
#             numero=int(input(mensaje_error))  


def validate_number(mensaje: str, mensaje_error: str, minimo: int, maximo: int) -> int:
    while True:
        numero = int(input(mensaje))
        if minimo <= numero <= maximo:
            return numero  # Devuelve el número si está dentro del rango
        else:
            print(mensaje_error)  # Imprime el mensaje de error si no está en el rango
        
            print("Error: ingrese un número válido.")  # Maneja el caso donde no se ingresa un entero

# respuesta = validate_number("ingrese un numero: ", "error ingrese nuevamente un numero: ", 1, 10)

# print("la respuesta es", respuesta)


def validate_length(mensaje: str, longitud: int) -> str:
    while True:
        cadena = input(mensaje)  # Pide la cadena usando el mensaje personalizado
        if len(cadena) == longitud:
            return cadena  # Retorna la cadena si la longitud es correcta
        else:
            print(f"Error: la cadena debe tener exactamente {longitud} caracteres. Inténtelo de nuevo.")