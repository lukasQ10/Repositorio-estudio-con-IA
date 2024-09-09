
"""
print("\nPROGRAMA PARA CALCULAR EL ÁREA DE UN POLÍGONO:")

def calculo(base, altura):
    if base == 0 or altura == 0:
        return "Ni la base ni la altura pueden ser de valor '0'; intentelo de nuevo..."
    else:  
        return base * altura

while True:
    base = float(input("Ingrese por favor la base: "))        
    altura = float(input("Ingrese por favor la altura: "))

    resultado = calculo(base, altura)
    
    if isinstance(resultado, str):  # Verifica si el resultado es un mensaje de error
        print(resultado)
    else:
        print(f"El área del polígono es: {resultado}")
        break  # Sale del bucle si la entrada es válida
if __name__ == "__main__":
    calculo(base, altura)

"""
"""
# PROGRAMA QUE DEVUELVE LA SUMA DE LOS NUMEROS POSITIVOS DE UNA LISTA:

def suma_positivos(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero > 0:
            suma += numero
    return suma

# Ejemplo de uso
lista = [1, -2, 3, -4, 5]
print(suma_positivos(lista))  # Output: 9
"""


# PROGRAMA QUE PERMITE DIVIDIR DOS NUMEROS Y CAPTURA EL ERROR SI SE DIVIDE POR CERO:

def divisible(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        print("Error: En numero divisible no puede ser cero; intentelo de nuevo") 


casa = 45
perro = 45465
casa = 48
arbol = 65465
avion = 65
perro = 8458465

# > "lsadas" lñlasñ kk