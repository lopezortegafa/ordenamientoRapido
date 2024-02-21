def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [x for x in arr[1:] if x <= pivote]
        mayores = [x for x in arr[1:] if x > pivote]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

def imprimir_arreglo(arreglo):
    print("Arreglo ordenado:", arreglo)

def obtener_arreglo():
    arreglo = []
    n = int(input("Ingrese la cantidad de elementos del arreglo: "))
    for i in range(n):
        elemento = float(input(f"Ingrese el elemento {i + 1}: "))
        arreglo.append(elemento)
    return arreglo

