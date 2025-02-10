from random import randrange
import math


def pesquisa_binaria(lista, index):
    baixo = 0
    alto = len(lista) - 1
    max = int(math.log(alto, 2))
    tentativas = 0
    while baixo <= alto:
        tentativas=tentativas+1
        meio = int((baixo + alto) / 2)
        chute = lista[meio]

        
        if chute == index:
            print("Nº de tentativas: "+ str(tentativas)+" do máximo: "+str(max))
            return meio

        if chute > index:
            alto = meio - 1
        else: 
            baixo = meio + 1

   
    print("Nº de tentativas: "+ str(tentativas)+" do máximo: "+str(max))
    return None




def main():

    # qtd = randrange(0, 1001)
    # lista = []
    # for i in range(1, qtd):
    #     lista.append(randrange(0, 1001))
    # lista.sort();
    # a = set(lista)
    # lista_ordenada = list(a)
    # index = randrange(0, 101)

    lista_ordenada = []
    for i in range(1, 101):
        lista_ordenada.append(i)

   

    retorno = pesquisa_binaria(lista_ordenada, 75)
    # print("A lista é formado por: "+ str(lista_ordenada))
    texto = "A quantidade de itens é "+ str(len(lista_ordenada))+ " sendo a busca do número: "+ str(75) + " sendo a posição: " + str(retorno)+ "."
    print(texto)

    print()

    retorno2 = pesquisa_binaria(lista_ordenada, 35)
    # print("A lista é formado por: "+ str(lista_ordenada))
    texto = "A quantidade de itens é "+ str(len(lista_ordenada))+ " sendo a busca do número: "+ str(35) + " sendo a posição: " + str(retorno2)+ "."

    print(texto)

if __name__ == "__main__":
    main()