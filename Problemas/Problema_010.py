## Problema 010 - Suma de primos
# Enunciado: https://projecteuler.net/problem=10
# Nivel de dificultad: d = 0
# Puntos: p(d,n) = 1
# Tiempo observado en Colab (CPU):
# Estrategia: Primero definir los primos, la definición de los primos la busque en youtube y google, luego
# hacer una lista vacia donde se logre agregar cada uno de los números primos en el rango que se nos solicite
# y luego sumar cada uno de los primos que se añadan a la lista.


def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):   #Esta definicion de primos la encontré en youtube
        if num % i == 0:
            return False
    return True

primos = []                     # Una lista vacia
for n in range(2, 2000000):     # Un rango que va desde el 2 hasta por debajo del número recorrido
    if es_primo(n):
        primos.append(n)        # Lo añadimos a las lista para luego sumar todos esos datos
suma = sum(primos)
print(f"{suma}")