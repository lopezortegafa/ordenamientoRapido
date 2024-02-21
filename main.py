import ordenamiento_rapido
from ordenamiento_rapido import imprimir_arreglo, obtener_arreglo, quick_sort

def main():
    arreglo = obtener_arreglo()
    arreglo_ordenado = quick_sort(arreglo)
    imprimir_arreglo(arreglo_ordenado)

if __name__ == "__main__":
    main()

