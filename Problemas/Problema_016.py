## Problema 016 - Suma de digitos de potencia
# Enunciado: https://projecteuler.net/problem=16
# Nivel de dificultad: d = 0
# Puntos: p(d,n) = 1
# Tiempo observado en Colab (CPU):
# Estrategia: Primero definir nuestra variable x que elevaremos a la potencia deseada, despues
# convertir el resultado de esa potencia en un formato de texto, para despues pasar por cada 
# uno y sumar sus valores, conviertiendolo a valores numericos.


def funcion():
    x = 2
    total = 0
    for y in range(1000, 1001):
        potencia = x**y
        digitos = str(potencia)     # Esta funcion hace que a la potencia 2**1000, tome los 
                                    # los digitos y los convierta en letras primero
        for d in digitos: 
             digitos_suma = int(d)  # y en esta parte los convierta en datos numericos para
             total += digitos_suma  # luego sumarlos todos
        
    return total
resultado = funcion()
print(f"{resultado}")
