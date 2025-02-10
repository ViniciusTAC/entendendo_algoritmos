def maximo(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    max = maximo(lista[1:])
    return lista[0] if lista[0]> max else max


def main():
    # lista = [3,1,4,5,2]
    lista = [[34, 7, 23, 32, 5, 62, 78, 10],
    [89, 12, 56, 45, 67, 90, 11, 32],
    [4, 19, 27, 33, 50, 2, 89, 101],
    [99, 87, 45, 23, 12, 55, 68, 74],
    [200, 43, 87, 92, 150, 32, 71, 10],
    [11, 29, 37, 88, 42, 91, 65, 77],
    [5, 17, 39, 64, 82, 100, 47, 13],
    [72, 54, 92, 33, 45, 29, 87, 11],
    [1, 99, 58, 36, 72, 44, 25, 67],
    [6, 18, 38, 50, 97, 23, 89, 77]]

    for i in lista:
        resultado = maximo(i)
        texto = f"\nO Maior Valor Recursivo da lista {i} é {resultado}."

        print(texto)

if __name__ == "__main__":
    main()
