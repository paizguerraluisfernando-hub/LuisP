## Problema 017 - Número de letras
# Enunciado: https://projecteuler.net/problem=17
# Nivel de dificultad: d = 2
# Puntos: p(d,n) = 11
# Tiempo observado en Colab (CPU):
# Estrategia: Primero utilizando una libreria externa para obtener la forma literal(en ingles) de los números
# que se nos solicitan, luego añadirlos a una lista vacia para luego contar cuantas letras contiene ese
# rango numerico. 

#Como una nota adicional la libreria utilizada y lo relacionado a ella lo encontre en Youtube
from num2words import num2words
lista = []                          # Esta parte permite utilizar la libreria num2words en ingles para
for x in range(1, 1001):            # obtener la forma literal de los números, quitandole guiones y espacios
    lista.append(num2words(x, lang = 'en').replace('-','').replace(' ',''))
    
letras = []
for indice in lista:                # Esta parte añade los elementos a la lista vacia de manera separada
    for l in indice:                # para posteriormente leer cuantos elementos tiene la lista "letras"
        letras.append(l)

cantidad = len(letras)
print(cantidad)