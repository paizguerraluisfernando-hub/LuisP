## Problema 020 - Suma factorial de digitos
# Enunciado: https://projecteuler.net/problem=20
# Nivel de dificultad: d = 0
# Puntos: p(d,n) = 1
# Tiempo observado en Colab (CPU):
# Estrategia: Utilizando la definición de factorial, encontramos el número que se nos solicita
# luego definimos un bucle con el resultado convertido en texto para despues sumar cada caracter
# o digitos convertido ya en forma numerica.


def factorial(n):
    if n < 0:
        raise ValueError("n no debe ser negativo")
    if n == 0:
        return 1
    return n * factorial(n - 1)                     # Esta definicion de factorial fue brindada en una clase
total = 0
for resultado in str(factorial(100)):               # convertimos el resultado del factorial en texto para
    for d in resultado:                             # luego convertirlo en texto y sumar cada uno de los
        sumat = int(d)                              # digitos
        total += sumat
print(total)
        
        
    
  




    
