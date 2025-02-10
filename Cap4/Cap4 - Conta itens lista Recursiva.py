
from random import randrange
def conta(lista):
   if lista ==  []:
       return 0
   else:
       return 1 + conta(lista[1:])
    

def main():
    lista = []
    qtd = 9
    for i in range(0, qtd):
        lista.append(i+1)
    resultado = conta(lista)
    texto = f"A Contagem Recursiva dos itens da lista {lista} é igual a {resultado}."

    print(texto)

if __name__ == "__main__":
    main()
