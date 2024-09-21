
# PROGRAMA PARA CALCULAR EL AREA DE UN POLIGONO
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

# PROGRAMA QUE DEVUELVE LA SUMA DE LOS NUMEROS POSITIVOS DE UNA LISTA:

"""
def suma_positivos(lista_numeros):   # funcion para trabajar la lista numeros
    suma = 0        # variable que se actualizara que por defecto se inica en '0'
    for i in lista_numeros:   # bucle que recorre lista_numeros y almacena en 'i'
        if i > 0:   # Si i es un numero positivo osea mayor a cero, osea no es -1 o algo asi
            suma += i     # Entonces suma cada uno de esos numeros; cada vez que encuentra uno positivo al anterior lo suma
    return suma    # retorna la suma de esos numeros que no son negativos osea todos los que sean mayores a cero


lista = [1, -2, 3, -4, 5, 15]
print(suma_positivos(lista))  # Output: 9
"""

# PROGRAMA QUE PERMITE CREAR UNA SECUENCIA FIBONACCI

"""def fibonacci(n):
    a, b = 0, 1
    lista_numeros_fibonacci = []  # Lista para almacenar la serie de Fibonacci
    
    for _ in range(n):
        lista_numeros_fibonacci.append(a)  # Agregar el número actual a la lista
        a, b = b, a + b  # Actualizar los valores de a y b
    
    return lista_numeros_fibonacci

print(fibonacci(10))
"""

"""
def fibonacci(n):
    a,b = 0, 1
    lista_vacia = []
    for _ in range(n):
        lista_vacia.append(a)
        a,b = b, a+b # <---- esta parte a que linea actualiza a la segunda linea de codigo arriba? ya que append solo agreda a 'a' y no a 'b'
    return lista_vacia

print(fibonacci(15))
"""    



"""
def fibonacci2(n):
    a, b = 0, 1
    lista_fibo = []
    for _ in range(n):
        lista_fibo.append(a)
        a, b = b, a+b
    return lista_fibo

print(fibonacci2(25))    
"""


"""
from functools import lru_cache

fibonacci_lambda = lru_cache(None)(lambda n: n if n < 2 else fibonacci_lambda(n-1) + fibonacci_lambda(n-2))
print(fibonacci_lambda(10))
"""


"""
def fibo(n):      # Funcion recibe un numero por parametro
    a,b = 0, 1       #  se definen las variables primarias con sus valores
    lista_fibo = []    # se crea una variable con una lista vacia para ser llena
    for _ in range(n):    # Se itera las veces que se pasen por parametro en una variable que no se llama, solo itera
        lista_fibo.append(a)   # Se agrega a la lista vacia el primer valor de 'a'
        a,b = b, a+b        # Se actualiza el valor de a en la segunda linea del codigo para luego ser agregada actulizada a la lista
        
    return lista_fibo

print(fibo(10))

"""

# PROGRAMA QUE RECORRE UNA LISTA Y MUESTRA CUAL ES EL NUMERO MAYOR DE TODA LA LISTA


def encontrar_mayor(lista):  # 'lista' es un parámetro genérico
    num_mayor = lista[0]         # num_mayor es igual al primer numero de la lista 'numeros' osea el '3'
    for i in lista:        # Recorremos la lista y guardamos en 'i'
        if i > num_mayor:      # si i es un numero mayor que num_mayor
            num_mayor = i      # Entonces num_mayor se actualiza a ese numero mayor de i, y solo se va actulizando hasta encontrar el numero mayor
    return num_mayor          # num_mayo actualizado al numero mayor que haya encontrado y lo envia como respuesta

numeros = [3, 5, 7, 2, 8, -1, 4, 10, 12]
print(encontrar_mayor(numeros))  # Se pasa 'numeros' como argumento a 'lista'



def mayor(lista):
    num_mayor = lista[0]
    for i in lista:
        if i > num_mayor: 
            num_mayor = i
    return num_mayor        

numeros = [2,5,15,-56,12,95]
print(mayor(numeros))


# PROGRAMA QUE PIDE NOMBRE AL USUARIO, CALCULE SU EDAD A PARTIR FECHA NACIMIENTO, 
# IMPRIME MENSAJE CON SU NOMBRE Y EDAD
# Y VERIFIQUE SI ES MAYOR DE EDAD Y MUESTRE UN MENSAJE ADECUADO.
"""
from datetime import date

nombre = input("Ingrese su nombre por favor: ")
fecha_nacimiento = int(input("Ingrese fecha nacimiento sin puntos ni comas comenzando por el año, mes y día: "))
def datos (nombre, fecha_nacimiento):
    fecha_actual = date.today()
    if fecha
    
"""


