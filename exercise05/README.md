*Exercício 05: Interface entre C++, ROOT e Python*

->Parte 1: C++ e ROOT (Compilação)
**O que `root-config --cflags` e `root-config --libs` retornam e por que o compilador precisa disso?**
Os comandos retornam os caminhos para os ficheiros de cabeçalho e as diretivas de ligação para as bibliotecas dinâmicas do ROOT instaladas no sistema. O compilador C++ precisa desta informação para saber onde encontrar a definição e a implementação das classes utilizadas (como `TTree`), um passo que não era necessário no interpretador do ROOT já que esse carrega esses dicionários automaticamente na memória.

->Parte 2: Python e ROOT (PyROOT)
**Como acontece o elo entre o Python e as bibliotecas compiladas do ROOT em C++?**
O PyROOT não é uma reescrita do ROOT em Python, mas sim uma conexão. Quando chamamos `ROOT.TTree()` no Python, o módulo cuida de carregar a biblioteca original em C++ e invoca as classes nativas, servindo apenas como uma ponte de comunicação 

->Parte 3: Comparando as três versões

|       Característica 	      |    Macro do ROOT (Interpretado)   |               C++ Compilado 	       |           PyROOT (Script Python) 		|
|:---------------------------:|:---------------------------------:|:------------------------------------------:|:----------------------------------------------:|
| **Mais rápida de escrever** | Média                		  | Mais lenta (exige estruturação)            | Mais rápida (sintaxe limpa) 			|
| **Mais rápida de executar** | Média                		  | Mais rápida (código máquina nativo)        | Mais lenta (interpretador + overhead de ponte) |
| **Deteção de erros de tipo**| Em tempo de execução 		  | Em tempo de compilação (antes de rodar)    | Em tempo de execução 				|
|:---------------------------:|:---------------------------------:|:------------------------------------------:|:----------------------------------------------:|


