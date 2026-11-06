## Problema 013 - Large Sum
# Enunciado: https://projecteuler.net/problem=13
# Nivel de dificultad: d = 1
# Puntos: p(d,n) = 3
# Tiempo observado en Colab (CPU):
# Estrategia: Definimos una lista donde podamos añadir cada uno de los datos para luego sumar todos por
# completo y luego convertir la suma a texto y selccionar los primeros 10 digitos


lista = []
f = open("numeros_013.txt")
leer = f.read().split()
for n in leer:
    x = int(n)
    lista.append(x)
suma = sum(lista)
t = str(suma)
y = t[0:10]
    
print(y)