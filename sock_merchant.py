# CREADO POR GITHUB: CHANGO01

# Problema de Hackerrank adaptado, copiar SOLO FUNCIÓN de este código en el link de abajo y funciona en hackerrank.
# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def sock_merchant(n,arr):       # función con parámetro de cantidad de medias y la lista.
    arr.sort()                  # ordeno de menor a mayor así quedan ordenados y es mas sencillo el agrupamiento.
    suma=0                      # variable que va a sumar los pares.
    i=1
    while i<n:
        if arr[i-1]==arr[i]:    # voy comparando de grupos de dos, si son pares sumo dos posiciones al indice y sino solo una posición.        
            suma+=1
            i+=2
        else:
            i+=1    
    return suma

n=int(input("Ingrese cantidad de medias: "))        # input para cantidad de medias.
arr=[]                                              # lista vacía.
for i in range(n):                                  # lleno la lista con valores enteros que representan los colores.
    valor=int(input("Ingrese número que indica color de media, puede repetir: "))
    arr.append(valor)
resultado=sock_merchant(n,arr)                      # llamo a la función.
print(resultado)                                    # cantidad de pares de media por color.
        