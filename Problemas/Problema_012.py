## Problema 012 - Número triangular altamente divisible
# Enunciado: https://projecteuler.net/problem=12
# Nivel de dificultad: d = 1
# Puntos: p(d,n) = 3
# Tiempo observado en Colab (CPU):
# Estrategia: Definir los primos, con una función que investigue pero modificandola para que tome cada
# valor y empiece a revisar cual es el que tiene 500 divisores, si tiene menos o más no los toma y pasa 
# al siguiente utilizando la suma de los números triangulares.


def funcion_d(x):
    d = 0
    for i in range(1, int(x**0.5) + 1):     # Toma los números de la función que sigue, y va contando
        if x % i == 0:                      # cual es el que tiene 500 divisores
            d += 1
            if i != x//i:
                d += 1
    return d
def numero(m):                              # Esta es la función que toma los numeros triangulares 
    n = 1                                   # y los pasa a la funcion_d para que tome cual es el número
    while True:                             # que tiene 500 divisores 
        triangular = (n * (n + 1)) // 2
        if funcion_d(triangular) > m:
            return triangular
        n += 1
resultado = numero(500)
print(resultado)