#Entrada: Un array de n numeros, en orden arbitrario.
#Salida: un array con los mismos numeros, ordenados de menor a mayor.
#ejemplo: [5, 4, 2, 1, 8, 7, 2, 6, 3] => [1, 2, 2, 3, 4, 5, 6, 7, 8]

entrada = [5, 4, 2, 1, 8, 7, 2, 6, 3]

def merge_sort(arr):
    left_arr = []
    right-arr = []