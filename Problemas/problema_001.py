## Problema 001 - Multiplos de 3 o 5
# Enunciado: https://projecteuler.net/problem=1
# Nivel de dificultad: d = 0
# Puntos: p(d,n) = 1
# Tiempo observado en Colab (CPU):
# Estrategia: generar dos listas, una para todos los múltiplos de 3 y la otra los múltiplos de 5
# para ambas listas hacer un recorrido hasta donde se solicita, utilizando saltos y almacenar ese recorrido
# y luego sumar ambas listas sin que los datos, como 15, se repitan y luego sumar los datos de la nueva lista


lista_3 = []
for x in range(3, 1000, 3):
  lista_3.append(x)           # Hacer las lista de los múltiplos de 3,  dando saltos de 3 en 3


lista_5 = []
for y in range(5, 1000, 5):
  lista_5.append(y)          # Hacer una lista de los múltiplos de 5, dando saltos de 5 en 5


lista = set(lista_3 + lista_5)    # Sumar ambas listas, y usar "set" para que los datos iguales no se
                                  # repitan como por ejemplo el 15

suma = sum(lista) # Sumar todos los datos de la nueva lista
print(suma)