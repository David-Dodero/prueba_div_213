#1. Realizar una función recursiva que calcule la suma de los primeros números naturales:
def sumar_naturales(numero: int)-> int:

    if numero == 0 :
        return 0 
    else:
        return numero + sumar_naturales(numero - 1 )
    
resultado= sumar_naturales(5)
print(resultado)
