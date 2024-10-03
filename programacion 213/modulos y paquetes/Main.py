# formas de importar modulos

# import funciones

# funciones.saludar("Hola a todos")
# print(funciones.mensaje_inicial)

# from funciones import saludar  
# saludar("que ondaaa")

# from funciones import saludar, saludar_alumno  
# saludar("que ondaaa")
# print(saludar_alumno("El Deivo", "bienvenido"))

# from funciones import*
# saludar("zapeee")
# saludar_alumno("Dvid","esaaaa")
# saludar_profesor("flapshap","rafh")

# from package_funciones import funciones

# funciones.saludar("Hola a todos")

#como ahora funciones esta en package_funciones tengo que entrar primero a package_funciones con un from y depues importar funciones
# from package_funciones import funciones
# funciones.saludar_alumno("pepe", "como vai?") 

# print(funciones.mensaje_inicial)
# #as es un alias para package_funciones.funciones
# import package_funciones.funciones as FC

# print(FC.mensaje_final)

# import random 

# numero_aleatorio= random.randint(1,28)
# print(numero_aleatorio)

#actividad 1 de paquetes
from package_funciones.pedir_numero import get_int

resultado= get_int("ingrese un numero entero: ", "errorazo ingrese un numero entero: ", 1, 10, 5)

print("el resultado es",resultado)  

 
from package_funciones.pedir_numero import get_float

resultado2= get_float("ingrese un numero flotante: ", "errorazo ingrese un numero entero: ", 0.5, 10.5, 5)

print("el resultado2 es",resultado2)  

from package_funciones.pedir_numero import get_string 

resultado3 = get_string(5)  # Por ejemplo, se espera una cadena de longitud 5
print("Cadena ingresada:", resultado3)