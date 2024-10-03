#1. Realizar una función recursiva que calcule la suma de los primeros números naturales:
# def sumar_naturales(numero: int)-> int:

#     if numero == 0 :
#         return 0 
#     else:
#         return numero + sumar_naturales(numero - 1 )
    
# resultado= sumar_naturales(5)
# print(resultado)

# 2. Realizar una función recursiva que calcule la potencia de un número:
# def calcular_potencia(base: int, exponente: int)->int:
    
#     if exponente == 0:
#         return 1
#     else:
#         return base * calcular_potencia(base, exponente - 1)
    
# resultado = calcular_potencia(2,5)
# print(resultado)


#3. Realizar una función recursiva que permita realizar la suma de los dígitos de un número:

def sumar_digitos(numero: int)-> int:
    
    if numero == 0:
        return 0
    else:
        return (numero % 10) + sumar_digitos(numero // 10)
    
resultado = sumar_digitos(544)

print(resultado)


#a partir de aca 
# Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La
# función deberá seguir el siguiente prototipo  
# número: el número ingresado por el usuario mediante consola, utilizando nuestra función
# get_int(mensaje,mensaje_error,mínimo,máximo,reintentos)


# def get_int(mensaje,mensaje_error,minimo,maximo,reintentos):
#     intentos= 0
#     while intentos < reintentos:
#         try:
#             numero = int(input(mensaje))
#             if minimo <= numero <= maximo:
#                 return numero
#             else:
#                 print(mensaje_error)
#         except ValueError:  # Maneja el caso donde la entrada no es un número
#             print(mensaje_error)
#         intentos += 1
#     return None  # Devuelve None si se superan los intentos


# def calcular_fibonacci(numero:int)-> int:

#     if numero == 0:  # Caso base
#         return 0
#     elif numero == 1:  # Caso base
#         return 1
#     else:
#         return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2) 


# numero= get_int(mensaje="Ingresa un número para calcular el Fibonacci: ",
#     mensaje_error="Error: Debes ingresar un número entero entre 0 y 20.",
#     minimo=0,
#     maximo=20,
#     reintentos=3)


# if numero != None:
#     resultado = calcular_fibonacci(numero)
#     print(f"El número de Fibonacci en la posición {numero} es {resultado}")
# else:
#     print("No se ingresó un número válido.")