## Problema 025 - 1000-digits Fibonacci number
# Enunciado: https://projecteuler.net/problem=25
# Nivel de dificultad: d = 1
# Puntos: p(d,n) = 3
# Tiempo observado en Colab (CPU):
# Estrategia: definir una función de fibonacci, para introducir un bucle que lea cuantos son los digitos
# que posee el número actual de la secuencia y un contador que explique cual es el número de veces que hizo
# este proceso hasta encontrar el número correcto


def fib():
    a = 0
    b = 1
    n = 1
    while len(str(b)) < 1000:
        c = b + a
        a = b
        b = c                   # Investigue muchas definiciones de Fibonacci pero ninguna me convencio
        n += 1                  # me costo un poco definirlo para luego usar un bucle infinito que pare 
    return n                    # cuando los digitos superen a 1000 y contar en que momento sucedio.
resultado = fib()
print(f"{resultado}")