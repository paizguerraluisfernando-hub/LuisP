## Problema 030 - Quinta potencia del digito
# Enunciado: https://projecteuler.net/problem=30
# Nivel de dificultad: d = 0
# Puntos: p(d,n) = 1
# Tiempo observado en Colab (CPU):
# Estrategia: Primero definir la manera en que los digitos a la quinta son iguales a ese mismo numero
# tambien si el número si resulta cumplir esta condición almacenarlo y esperar para encontrar a otro para
# sumar todos 


lista = []
total = 0
for x in range(2, 200000): # El rango es hasta 200mil, entre más grande o pequeño los números son los mismos valores
    digitos = sum(int(digito)**5 for digito in str(x))
    if x == digitos:
        total = total + x                       # En esta parte se coloca la condicion de que los digitos
                                                # al elevarlos a la quinta sean iguales a ese mismo nuúmero
        lista.append(total)                     # en todo caso si suceda se almacena y se van guardando en la 
print(max(lista))                               # lista vacia hasta encontrar el maximo
        
        
        