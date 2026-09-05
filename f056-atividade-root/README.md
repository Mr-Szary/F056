# Atividade: Introdução ao ROOT (TTree, TFile e Histogramas)

Este repositório usa o ROOT para gerar, armazenar e ajustar dados simulados utilizando `TTree` e `TFile`.

#Como executar

1.Geração dos dados (`generate.C`)**
   Este script gera 1000 números aleatórios seguindo uma distribuição gaussiana e os salva no arquivo `dados.root`.
   Para rodar, utilize o comando:
   `root -l generate.C`

2.Leitura e Ajuste (`plot.C`)**
   Este script lê a árvore salva em `dados.root`, preenche um histograma, aplica o estilo visual (linha preta espessa, fundo amarelo) e realiza um ajuste gaussiano. O resultado é salvo como `histograma.png`.
   Para rodar, utilize o comando:
   `root -l plot.C`

#Comparação dos Parâmetros

Na geração dos dados, foram definidos os seguintes parâmetros exatos:
* **Média:** 0.0
* **Desvio-padrão (Sigma):** 1.0


