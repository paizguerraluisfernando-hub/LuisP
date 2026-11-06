## Problema 048 - Poderes propios
# Enunciado: https://projecteuler.net/problem=48
# Nivel de dificultad: d = 0
# Puntos: p(d,n) = 1
# Tiempo observado en Colab (CPU):
# Estrategia: Definimos una lista vacia, luego hacemos que la variable este en el rango que se nos pida
# y hacemos que se añada cada uno de los valores de la condicion que nos dice el ejercicio, y que se añada 
# en la lista vacia para luego sumarlo todo en una sola variable.


conjunto = []
for x in range(1, 1001):
  r = x**x
  conjunto.append(r)        # Se define la lista vacia y los valores que se añadiran a la lista
suma = sum(conjunto)        # La suma de todos los datos de la lista y como algo que no sabia y Abner me 
d = suma % (10**10)         # comentó es que si hacemos el modulo entre el número final y 10 a una potencia
                            # podemos encontrar los ultimos digitos, según a la potencia que este el 10
print(f"{d}")