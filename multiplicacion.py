#Entrada: dos enteros x e y de n digitos
#Salida: el producto de x * y
#Asunción: n es el número de dígitos en los números de entrada

# Multiplicación de dos números
def multiplicar(a, b):
    return a * b
#La complejidad de una multiplicacion es de O(1) 


#Multiplicación de Karatsuba
def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        half = n // 2

        a = x // 10**half
        b = x % 10**half
        c = y // 10**half
        d = y % 10**half

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        abcd = karatsuba(a + b, c + d)

        return ac * 10**(2 * half) + (abcd - ac - bd) * 10**half + bd
    
#La complejidad de Karatsuba es de O(n^log2(3)) aproximadamente O(n^1.585) 
#El tiempo de ejecución puede variar según la implementación y el tamaño de los números.

#Ejemplo de uso
print(multiplicar(1234, 5678))
print(karatsuba(1234, 5678))

#El metodo de Karatsuba es más eficiente para números grandes en comparación con la multiplicación tradicional.

#Para números pequeños, la multiplicación tradicional puede ser más rápida debido a la sobrecarga de las llamadas recursivas en Karatsuba.

#Conclusión: La elección del método de multiplicación depende del tamaño de los números y del contexto en el que se utilicen.