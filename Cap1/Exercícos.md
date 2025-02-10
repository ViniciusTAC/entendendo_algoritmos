# Exercícios
### 1.1 Suponha que você tenha uma lista com 128 nomes e esteja fazendo uma pesquisa binária. Qual seria o número máximo de etapas que você levaria para encontrar o nome desejado?

**Resposta:** Utilizando a formula log <sub>2</sub> n, sendo n o número de tentativas, então log <sub>2</sub> 128 = 7


---

### 1.2 Suponha que você duplique o tamanho da lista. Qual seria o número máximo de etapas agora?

**Resposta:** Podemos usar o mesmo conceito de log <sub>2</sub> n, sendo log <sub>2</sub> 256 = 8. 

Ou usar a lógica de como vamos duplicar o número de tentativas, o resultado será +1, se 128 ao dobrar para 256 sera 8, assim como se for 512 sera 9. Isso so funciona por causa da base ser 2.

---
---
## Forneça o tempo de execução para cada um dos casos a seguir em termos da notação Big O

### 1.3 Você tem um nome e deseja encontrar o número de telefone para esse nome em uma agenda telefônica.
**Resposta:** No caso podemos usar a pesquisa binaria, sendo assim o tempo de execução seria O(log n), sendo n o numero de nomes na lista telefônica.

---

### 1.4 Você tem um número de telefone e deseja encontrar o dono dele em uma agenda telefônica. (Dica: Deve procurar pela agenda inteira!)

**Resposta:** Como neste temos é o numero, e não o nome, devemos procurar basicamente por toda lista, ja que o que esta ordenado pelo nome e não pelo número. Em outras palavras o tempo de execução é O(n), sendo n o número de nomes.

---

### 1.5 Você quer ler o número de cada pessoa da agenda telefônica.
**Resposta:**  Neste caso sem duvida vai ser O(n), ja que vamos ter que passar por todos os nomes.

---

### 1.6 Você quer ler os números apenas dos nomes que começam com A. (Isso é complicado! Esse algoritmo envolve conceitos que são abordados mais profundamente no Capítulo 4. Leia a resposta – você ficará surpreso!)
(Resposta apos a leitura do capitulo 4)