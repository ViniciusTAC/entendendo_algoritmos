def soma(lista):
    print(f"Chamada da pilha com a lista: {lista}")
    if lista == []:
        return 0
    else:
       x = lista[0] + soma(lista[1:])
       print(f"Soma ate o momento: {x}")
       return x
    

def main():
    lista = [1, 2, 3, 4, 5]
    resultado = soma(lista)
    texto = f"\n\nA Soma Recursiva da lista {lista} é igual a {resultado}."

    print(texto)

if __name__ == "__main__":
    main()
