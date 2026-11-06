## Problema 080 - Expansión digital de raíz cuadrada
# Enunciado: https://projecteuler.net/problem=80
# Nivel de dificultad: d = 3
# Puntos: p(d,n) = 8
# Tiempo observado en Colab (CPU):
# Estrategia: Primero tomar unicamente los decimales, convertirlo a texto y luego sumar cada uno, para 
# luego sumar todos los resultados

from decimal import Decimal, getcontext

def r():
    getcontext().prec = 102
    suma_total = 0
    for n in range(1, 101):
        raiz = Decimal(n).sqrt()            # utilizando la libreria Decimal para extraer unicamente los
                                            # decimales de las raices irracionales
        if raiz % 1 == 0:
            continue                        # Lo añadimos a una tupla para que tome los decimales que necesitamos
        digitos = raiz.as_tuple()[1]        # tomamos los primeros 100 decimales
        primeros = digitos[:100]
        suma_total += sum(primeros)     # sumamos todos en total 

    return suma_total

resultado = r()
print(f"{resultado}")