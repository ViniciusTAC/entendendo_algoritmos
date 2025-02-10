

def busca_menor(lista):
    menor = lista[0]
    menor_indice = 0
    for i in range (1, len(lista)):
        if lista[i] < menor:
          menor = lista[i]
          menor_indice = i

    return menor_indice

def ordenacao_selecao(lista):
    lista_ordenada = []
    menor = busca_menor(lista)
    for i in range (len(lista)):
        menor = busca_menor(lista)
        lista_ordenada.append(lista.pop(menor))

    return lista_ordenada

def main():

    lista = [5, 3, 6, 2, 10]
    texto = "A lista original: "+ str(lista)
    lista_ordenada = ordenacao_selecao(lista)
    texto += "\nO resultado é a lista ordenada: " + str(lista_ordenada)+ "."

    print(texto)

if __name__ == "__main__":
    main()


