#Este exercício modela a cinemática de partículas carregadas em detectores, explorando os conceitos de encapsulamento e herança em C++ para diferenciar dados experimentais brutos de dados simulados

#O codigo funciona em duas partes:

#1:Track (Classe Base): Representa o traço reconstruído a partir das medidas experimentais. Ela armazena o quadrimomento (E, px, py, pz) de forma estritamente privada e implementa métodos públicos para derivar o momento transverso (pT) e a pseudorapidez (eta). O algoritmo inclui um tratamento condicional no método de pseudorapidez para lidar com a singularidade matemática quando a partícula viaja exatamente sobre o eixo Z (onde pT = 0)

#2: SimTrack (Classe Derivada): Representa a "verdade simulada" de Monte Carlo. Ela herda publicamente a estrutura e os cálculos de Track e adiciona o armazenamento dos identificadores físicos (PDG ID) da própria partícula e da sua partícula-mãe. O construtor utiliza a lista de inicialização para repassar corretamente o quadrimomento à classe base

#Como compilar e testar:
#Navegue até a pasta do exercício e utilize o make para compilar as bibliotecas compartilhadas (libTrack.so e libSimTrack.so) com suas devidas ligações. O programa de teste vai validar instâncias normais e casos limites puramente longitudinais

#cd ../ex2_track
make
./testTrack
