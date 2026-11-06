## Problema 022 - Nombres puntuaciones
# Enunciado: https://projecteuler.net/problem=22
# Nivel de dificultad: d = 0
# Puntos: p(d,n) = 1
# Tiempo observado en Colab (CPU):
# Estrategia: Primero darle el valor a cada letra del abecedario excepto la "ñ", luego abrir el archivo
# con la lista de nombres para despues añadirlos a una lista ordenada alfabeticamente, donde se toma los
# valores de las letras, se multiplican por su posición en la lista y luego se suman todos esos resultados


import string

posicion = {}
letras = string.ascii_uppercase
for i in range(1, 27):
    valor = letras[i - 1]
    posicion[valor] = i                 # Esta parte la investigue en youtube, para darle el valor numerico a
                                        #  cada letra
f = open("demofile.txt")
bucle = f.read()
f.close()                               #  Esta parte nos ayuda a abrir el archivo "demofile" que contiene los
l = bucle.replace('"', '').split(',')   #  nombres a listar, y remplaza las comillas por espacios en blanco y 
                                        #  en forma de lista
def nombre(lista):
    bucle_orden = sorted(lista)
    total = 0
    for indice, nombre_1 in enumerate(bucle_orden, start=1):
        suma = sum(posicion.get(letra, 0) for letra in nombre_1)
        resultado = suma * indice       # Se toma cada una de las letras se suma el valor asignado anteriormente
                                        # y se le multiplica la posicion que tiene en la lista ordenada, para 
        total = total + resultado       #  luego sumar todos
    print(f"{total}")
nombre(l)
