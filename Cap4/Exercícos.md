## EXERCÍCIOS

---
###  4.1 Escreva o código para a função soma, vista anteriormente.
**Resposta:** Cap4 - Soma Recursiva.py


---
###  4.2 Escreva uma função recursiva que conte o número de itens em uma lista.
**Resposta:** Cap4 - Conta itens lista Recursiva.py

---
###  4.3 Encontre o valor mais alto em uma lista.
**Resposta:** Cap4 - Valor Maximo Recursivo.py


---
###  4.4 Você se lembra da pesquisa binária do Capítulo 1? Ela também é um algoritmo do tipo dividir para conquistar. Você consegue determinar o caso-base e o caso recursivo para a pesquisa binária?
**Resposta:** Caso-base: O caso-base ocorre quando o array contém apenas um elemento. Nesse caso, basta comparar o número pesquisado com esse único elemento. Se forem iguais, o número foi encontrado; caso contrário, ele não está no array.

Caso-recursivo: No caso recursivo, a busca continua dividindo o array ao meio. Se o número pesquisado for maior que o elemento central, a pesquisa continua na metade superior; se for menor, na metade inferior. A outra metade é descartada, e o processo se repete até encontrar o número ou esgotar as possibilidades.



---
### Quanto tempo levaria, em notação Big O, para completar cada uma destas operações?

### 4.5 Imprimir o valor de cada elemento em um array.
**Resposta:** O(n), pois tera que passar por cada um dos elementos do array

---
### 4.6 Duplicar o valor de cada elemento em um array.
**Resposta:**  O(n), pois tera que passar também por cada elemnento do array, sendo o diferente da **4.5** é a ação que ira duplicar o valor e não imprimir

---
### 4.7 Duplicar o valor apenas do primeiro elemento do array.
**Resposta:** O(1), pois so pegar o primeiro elemento array[0] e duplicar ser valor

---
### 4.8 Criar uma tabela de multiplicação com todos os elementos do array.
### Assim, caso o seu array seja [2, 3, 7, 8, 10], você primeiro multiplicará cada elemento por 2. Depois, multiplicará cada elemento por 3 e então por 7, e assim por diante.
**Resposta:** O(n²), pois tera que passar por cada elemnto do array, sendo n por n vezes, ja que multiplirar todos os elementos por todos os elementos, sendo n vezes n ou n ao quadrado. 