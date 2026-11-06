## Problema 029 - Distinct powers
# Enunciado: https://projecteuler.net/problem=29
# Nivel de dificultad: d = 1
# Puntos: p(d,n) = 3
# Tiempo observado en Colab (CPU):
# Estrategia: Primero hacer una lista donde poder almacenar los datos para luego contar, luego hacer dos
# rangos para a, b y ordenar la lista y elminar los elementos iguales.


lista = []
for x in range(2, 101):
   for i in range(2, 101):      # Hacer los dos rangos para añadir a la lista vacia, y posteriormente 
      y = x**i                  # ordenar y sacar los elementos copiados 
      lista.append(y)
total = sorted(set(lista))
print(len(total))