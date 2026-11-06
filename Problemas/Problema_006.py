## Problema 006 - Diferencia de suma cuadrada
# Enunciado: https://projecteuler.net/problem=6
# Nivel de dificultad: d = 0
# Puntos: p(d,n) = 1
# Tiempo observado en Colab (CPU):
# Estrategia: Definir una funcion que nos permita tomar hasta el número deseado, en ambas sumas que cada
# tiene una funcion definida estas funciones las investigue, y de esas funciones puedo sacar los números
# que e¿se nos solicitan y usando la funcion principal restamos los resultados de las otras dos funciones


def funcion(num):
    x = num
    a = ( (x * (x+1) )//2)**2               # Números triangulares al cuadrado
    b = ( (x * (x + 1) * (2*x + 1))//6)     # Suma de cuadrados 
    total = a - b                           # La resta de estos dos
    return a, b ,total
a, b, c = funcion(100)
print(c)                                    # El resultado de la resta

