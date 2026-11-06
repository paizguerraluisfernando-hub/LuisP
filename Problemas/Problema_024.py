## Problema 024 - permutaciones lexicograficas
# Enunciado: https://projecteuler.net/problem=24
# Nivel de dificultad: d = 2
# Puntos: p(d,n) = 6
# Tiempo observado en Colab (CPU):
# Estrategia: Buscando alguna libreria de permutaciones se encuentra itertools, en youtube se encuentra,
# para posteriormente aplicar la libreria en forma de permutaciones y ordenarla en otra lista 
# y luego buscar la posicion anterior a la 1millon, segun se el orden de las listas que inicia en 0


import itertools
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]          # Se convoca la libreria, y la lista de 0 a 9

orden = sorted(itertools.permutations(lista))   # esta nueva variable almacena todos los conjuntos permutados
posicion = orden[999999]                        # ordenandolos de menor a mayor y encontrando la permutacion
print(posicion)                                 # 1millon. 