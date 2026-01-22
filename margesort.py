#Entrada: Un array de n numeros, en orden arbitrario.
#Salida: un array con los mismos numeros, ordenados de menor a mayor.
#ejemplo: [5, 4, 1, 8, 7, 2, 6, 3] => [1, 2, 3, 4, 5, 6, 7, 8]

entrada_numeros = [5, 4, 1, 8, 7, 2, 6, 3]

def merge_sort(entrada): 
    #usando el operador slicing: left_arr = entrada [0 : largo de la entrada / 2]
    left_arr = entrada[: len(entrada) // 2]

        #usando el operador slicing: right_arr = entrada [largo de la entrada / 2 : largo maximo de la entrada]
    right_arr = entrada[len(entrada) // 2 : len(entrada)]

    left_arr.sort()
    right_arr.sort()

    #Entada:arrays ordenados C yD (ambos de logitud n/2)
    #Salida: array ordenado B (de logitud n)
    #Asuncion: n es par
    i = 0; j = 0; k = 0; n = len(entrada) - 1; result = []
    while k < n:
        if left_arr[i] <right_arr[j]:
            result.append(left_arr[i])
            i = i + 1
        else:
            result.append(right_arr[j])
            j = j + 1
        k = k + 1

    print(result)

    #No se porque el ultimo elemento no lo inserta pero se hizo el intento xd


#probando la funcion qlera
merge_sort(entrada_numeros)