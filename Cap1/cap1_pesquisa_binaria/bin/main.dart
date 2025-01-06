import 'dart:io';
import 'dart:math';

void main() {
  // Declarações de variaveis
  String? qtdLista;
  int qtd = 0;

  String? elementoString;
  int elemento = 0;

  int? index;
  String? continuarString;
  bool continuar = true;

  print("----- Pesquisa binária -----");

  while (continuar) {
    stdout.write("\nQuantos elementos haverá na lista? ");
    qtdLista = stdin.readLineSync();

    qtd = int.parse(qtdLista ?? '0');

    List<int> lista = [];

    for (var i = 1; i <= qtd; i++) {
      lista.add(i);
    }

    print("\nQuantidade de elementos da lista: $qtdLista.");
    print("Lista: $lista");

    stdout.write("\nElemento procurado? ");
    elementoString = stdin.readLineSync();

    elemento = int.parse(elementoString ?? '0');
    // print("\nElemento procurado: $elemento.");

    index = pesquisaBinaria(lista, elemento);
    if (index != null) {
      print("\nElemento $elemento está na posição: $index.");
    } else {
      print("\nElemento $elemento não esta presente na lista.");
    }
    print("\n----------------------------------");
    stdout.write("Deseja continuar? (S para Sim - N para Não): ");

    continuarString = stdin.readLineSync();
    if (continuarString != null) {
      if (continuarString.toUpperCase().contains("S")) {
        continuar = true;
      } else {
        continuar = false;
      }
    }
  }
  print("\n\nEncerrando pesquisa binária.");
}

int? pesquisaBinaria(List<int> lista, int elemento) {
  int maxTentativas = (log(lista.length) / log(2)).round();
  

  int tentativas = 0;

  int baixo = 0;
  int alto = lista.length - 1;
  int meio = 0;

  while (baixo <= alto) {
    meio = ((baixo + alto) / 2).round();

    int chute = lista[meio];
    
    if (chute == elemento) {
      print(
          "\nFoi necessária $tentativas tentativas de no máximo $maxTentativas tentativas.");
      return meio;
    }
    if (chute > elemento) {
      alto = meio - 1;
    } else {
      baixo = meio + 1;
    }
    tentativas += 1;

    // print("meio: $meio - chute: $chute");
  }
  print(
      "\nFoi necessária $tentativas tentativas de no máximo $maxTentativas tentativas.");
  return null;
}
