# CREADO POR GITHUB: CHANGO01

# Problema de Hackerrank adaptado, copiar SOLO FUNCIÓN y los parámetros de este código en el link de abajo y funciona en hackerrank.
# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def suma_valles(n,lista):               # función, entra longitud y valores del string.
    sea=0                               # variables sea que cuenta el recorrido y suma los valles.
    suma=0
    for i in range(n):
        if lista[i]=="U" and sea!=-1:
            sea+=1
        elif lista[i]=="U" and sea==-1:
            sea+=1
            suma+=1   
        elif lista[i]=="D":
            sea-=1
        else:
            continue
    return suma

ruta="UDDDUDUU"                         
n=8
resultado=suma_valles(n,ruta)
print("valles: ",resultado)

