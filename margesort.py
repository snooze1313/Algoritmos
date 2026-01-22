#Entrada: Un array de n numeros, en orden arbitrario.
#Salida: un array con los mismos numeros, ordenados de menor a mayor.
#ejemplo: [5, 4, 1, 8, 7, 2, 6, 3] => [1, 2, 3, 4, 5, 6, 7, 8]

entrada_numeros = [5, 4, 1, 8, 7, 2, 6, 3]

# Merge sort (ordenamiento por mezcla) - implementación recursiva.

# Entrada: una lista de números (o cualquier elemento comparable).
# Salida: una nueva lista con los mismos elementos ordenados de menor a mayor.

# Ejemplo: [5, 4, 1, 8, 7, 2, 6, 3] -> [1, 2, 3, 4, 5, 6, 7, 8]

def merge(left, right):
    """Combina dos listas ya ordenadas `left` y `right` y devuelve una lista ordenada.

    left, right: listas ordenadas
    devuelve: lista ordenada que contiene todos los elementos de left y right
    """
    i = j = 0
    result = []
    # recorrer ambas listas y tomar el menor elemento en cada paso
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # añadir los restos (si alguno quedó)
    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])
    return result


def merge_sort(entrada):
    """Ordena y devuelve una nueva lista usando merge sort.

    Características:
    - Estable: mantiene el orden relativo de elementos iguales.
    - Divide y conquista: O(n log n) tiempo en el peor caso.

    entrada: lista (puede estar vacía)
    retorna: nueva lista ordenada
    """
    # casos base: lista vacía o de un solo elemento ya está ordenada
    if entrada is None:
        return None
    if len(entrada) <= 1:
        return entrada[:]  # devolver copia para evitar aliasing

    mid = len(entrada) // 2
    left = merge_sort(entrada[:mid])
    right = merge_sort(entrada[mid:])
    return merge(left, right)


if __name__ == '__main__':
    # pequeños tests / demostración
    casos = [
        [],
        [1],
        [2, 1],
        [5, 4, 1, 8, 7, 2, 6, 3],
        [3, 3, 2, 1, 2, 3],
        [-1, 5, 0, -2, 3]
    ]

    esperados = [
        [],
        [1],
        [1, 2],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [1, 2, 2, 3, 3, 3],
        [-2, -1, 0, 3, 5]
    ]

    for c, e in zip(casos, esperados):
        salida = merge_sort(c)
        print(f'entrada: {c} -> salida: {salida}')
        assert salida == e, f"Error: expected {e} but got {salida}"

    print('Todos los tests pasaron correctamente.')
#probando la funcion qlera
marged = merge_sort(entrada_numeros)
print(marged)


