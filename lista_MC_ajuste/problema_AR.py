import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.integrate import quad
import os

# Garante que o diretório para as figuras exista
os.makedirs('figuras', exist_ok=True)

# Definição da PDF (Gaussiana normalizada)
def Gaussian(x, mu, sigma):
    return (1.0 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * ((x - mu) / sigma)**2)

def pdf_1(x):
    return Gaussian(x, 0.0, 1.0)

# Problema 1: Função geradora de aceitação-rejeição
def random_pdf(pdf, N, x_min, x_max, f_max):
    x_rand = []
    n_tries = 0
    while len(x_rand) < N:
        n_tries += 2
        x = random.uniform(x_min, x_max)
        y = random.uniform(0.0, f_max)
        
        if pdf(x) > y:
            x_rand.append(x)
            
    return np.array(x_rand), n_tries

# Problema 2: Testes com a distribuição normal
N = 10000
f_max = pdf_1(0.0) # O máximo da Gaussiana padrão ocorre em x = 0

# (a) Eficiência para [-5, 5]
x_min_a, x_max_a = -5.0, 5.0
amostras, n_tries_a = random_pdf(pdf_1, N, x_min_a, x_max_a, f_max)
eficiencia_obtida = N / ( n_tries_a /2 )


integral, _ = quad(pdf_1, x_min_a, x_max_a)
eficiencia_esperada = integral / ((x_max_a - x_min_a) * f_max)

print(f"--- Parte (a) ---")
print(f"Sorteios totais para {N} eventos [-5, 5]: {n_tries_a}")
print(f"Eficiência obtida: {eficiencia_obtida:.4f}")
print(f"Eficiência esperada: {eficiencia_esperada:.4f}\n")

# (b) Variação da eficiência nos intervalos
print(f"--- Parte (b) ---")
intervalos = [(-3, 3), (-5, 5), (-10, 10)]
for xmin, xmax in intervalos:
    _, tries = random_pdf(pdf_1, N, xmin, xmax, f_max)
    print(f"Intervalo [{xmin:3}, {xmax:3}]: Eficiência = {N/ (tries/2):.4f}")

# Loop de 100 repetições para o intervalo [-5, 5]
distribuicao_sorteios = []
for _ in range(100):
    _, tries = random_pdf(pdf_1, N, -5.0, 5.0, f_max)
    distribuicao_sorteios.append(tries)

# Gráfico da distribuição de sorteios
plt.hist(distribuicao_sorteios, bins=15, edgecolor='black', color='skyblue')
plt.xlabel('Número total de sorteios')
plt.ylabel('Frequência')
plt.title(f'Distribuição de sorteios para obter {N} eventos aceitos (100 repetições)')
plt.savefig('figuras/gauss_aceita_rejeita.png')
plt.clf()
