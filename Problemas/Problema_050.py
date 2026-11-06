## Problema 050 - Suma de primos consecutivos
# Enunciado: https://projecteuler.net/problem=50
# Nivel de dificultad: d = 3
# Puntos: p(d,n) = 8
# Tiempo observado en Colab (CPU):
# Estrategia: Usando la definicion de primo, definimos hasta donde queremos que llegue el rango de los pirmos
# y los añadimos a una lista vacia donde hacemos que se sumen todos los primos hasta formar la cadena
# que sea más grande de primos consecutivos

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True             # La definicion utilizada en otros problemas

limite = 1000000
primos = []
for n in range(2, limite):
  if es_primo(n):
    primos.append(n)        # definimos una lista de primos hasta el rango

set_primos = set(primos)
longitud = 0
primomayor = 0              # la lista de primos la ordenamos para que no se repitan datos y definimos sumas

for i in range(len(primos)):
  suma_acumulada = 0
  for j in range(i, len(primos)):   # Convertimos la lista en una rango numerico donde hacemos que se sumen
    suma_acumulada += primos[j]     # los valores hasta encontrar la cadena más grande si esa cadena supera 
                                    # el limite lo paramos
    if suma_acumulada >= limite:
      break

    if (j - i + 1) > longitud and suma_acumulada in set_primos:
      longitud = (j - i + 1)
      primomayor = suma_acumulada     # aqui hacemos que imprima la cadena más grande de primos consecutivos
                                      # en esta etapa repeti muchas veces el codigo, porque crei que eran primos
print(primomayor)                     # desde 2 hasta el final de la cadena, pero si inicia en dos la cadena no 
                                      # no es suficientemente grande porque vuelve la cadena par, de hecho la
                                      # la cadena más grande empieza en 7; 2,3 y 5 no funciona.