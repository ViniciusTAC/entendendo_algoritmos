print('------------------Algoritmo sobre Caso-base e caso recursivo------------------\n')
# Aprender sobre Caso-base e caso recursivo

def regresiva(i):
    if i == 0: # caso base
      return i;
    else: # caso recursivo
       print(i)
       regresiva(i-1)


regresiva(10)

print('\n\n------------------Algoritmo de pilha de chamada------------------')
# A pilha de chamada

def saudar(nome):
   print("---------Começo do saudar")
   print("Olá", nome)
   perguntar(nome)
   print("---------Fim do perguntar")
   
   print("---------Fim do saudar")

def perguntar(nome):
   print("---------Começo do perguntar")
   print("Como você esta "+nome+"?")
   tchau(nome)
   print("---------Fim do tchau")

def tchau(nome):
   print("---------Começo do tchau")
   print("Tchau ", nome)

saudar("vinicius")