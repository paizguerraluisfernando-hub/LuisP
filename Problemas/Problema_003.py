## Problema 003 - Mayor factor primo
# Enunciado: https://projecteuler.net/problem=3
# Nivel de dificultad: d = 0
# Puntos: p(d,n) = 1
# Tiempo observado en Colab (CPU):
# Estrategia: Definir el número al cual buscaremos los factores, luego utilizando modulos encontrar
# los factores primos de este número agregandolo a una lista vacia y encontrando el maximo entre ellos 

x = 600851475143            # El número definido en x
lista = []                  # Una lista vacia
for i in range (1, 10000):  # El rango desde el uno hasta donde se nos solicita
    if x % i == 0:
        lista.append(i)   
print(max(lista))           # Se añade a la lista vacia donde se busca el maximo    
# Como algo adicional el rango esta de 1 hasta 10mil porque el código tambien toma los productos de los
# facotres principales como un factor adcional, el resultado 6857 es el factor primo más grande, los que 
# siguen son producto de los factores                      