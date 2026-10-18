import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
from scipy.optimize import brentq

# Problema 1: Histograma do tempo de decaimento
with open('decay.txt', 'r') as f:
    lines = (line.strip() for line in f if line.strip())
    t = [float(line) for line in lines]

fig, axis = plt.subplots(ncols=2, figsize=(12, 6))
axis[0].hist(t, bins=50)
axis[0].set(xlabel='t [s]', ylabel='N')
axis[0].set_title("Histograma")

counts_obs, bin_edges_obs = np.histogram(t, 50)
bin_centres_obs = (bin_edges_obs[:-1] + bin_edges_obs[1:]) / 2.0
err = np.sqrt(counts_obs)
axis[1].set_title("Histograma com Barras de Erro")
axis[1].errorbar(bin_centres_obs, counts_obs, yerr=err, fmt='o')
axis[1].set(xlabel='t [s]', ylabel='N')
plt.tight_layout()
plt.savefig("E2_Problem_1.pdf")
plt.clf()

# Problema 2: PDF Exponencial Teórica e Cálculo de Probabilidade
def decay_pdf(t_val, tau):
    return (1.0 / tau) * np.exp(-1.0 * t_val / tau)

x_p2 = np.linspace(0.0, 10.0, 1000)
f1 = decay_pdf(x_p2, 1.0)
f2 = decay_pdf(x_p2, 2.0)
f3 = decay_pdf(x_p2, 0.5)

plt.plot(x_p2, f1, label=r"$\tau = 1.0$ s")
plt.plot(x_p2, f2, label=r"$\tau = 2.0$ s")
plt.plot(x_p2, f3, label=r"$\tau = 0.5$ s")
plt.xlabel('t [s]')
plt.ylabel('f(t; τ)')
plt.legend(loc="upper right")
plt.savefig("E2_Problem_2.pdf")
plt.clf()

prob_p2 = integrate.quad(lambda val: decay_pdf(val, 2.0), 0.0, 1.0)[0]
print(f"P(t <= 1s | tau=2.0) = {prob_p2 * 100:.2f}%")

# Problema 3: Função de Verossimilhança para Medida Única (N=1, t=1)
def Likelihood(tau, N, sum_t):
    return ((1.0 / tau) ** N) * np.exp(-sum_t / tau)

x_p3 = np.linspace(0.5, 1.5, 1000)
L1 = Likelihood(x_p3, 1, 1.0)

plt.plot(x_p3, L1)
plt.xlabel(r'$\tau$ [s]')
plt.ylabel(r'$L(\tau)$')
plt.savefig("E2_Problem_3.pdf")
plt.clf()

# Problemas 4 e 5: Ajuste de Máxima Verossimilhança Não Binado (-2 ln L)
def lnL(tau, N, sum_t):
    return -2.0 * N * np.log(tau) + 2.0 * sum_t / tau

N_obs = len(t)
sum_t_obs = sum(t)
tau_hat = sum_t_obs / N_obs

x_p4 = np.linspace(max(0.1, tau_hat - 1.0), tau_hat + 1.0, 2000)
logLikelihood = lnL(x_p4, N_obs, sum_t_obs)

plt.plot(x_p4, logLikelihood)
plt.xlabel(r'$\tau$ [s]')
plt.ylabel(r'$-2 \ln L(\tau)$')
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate
from scipy.optimize import brentq

# Problema 1: Histograma dos dados
with open('decay.txt', 'r') as f:
    lines = (line.strip() for line in f if line.strip())
    t = [float(line) for line in lines]

fig, axis = plt.subplots(ncols=2, figsize=(12, 6))
axis[0].hist(t, bins=50)
axis[0].set(xlabel='t [s]', ylabel='N')
axis[0].set_title("Histograma")

counts_obs, bin_edges_obs = np.histogram(t, 50)
bin_centres_obs = (bin_edges_obs[:-1] + bin_edges_obs[1:]) / 2.0
err = np.sqrt(counts_obs)
axis[1].set_title("Histograma com Barras de Erro")
axis[1].errorbar(bin_centres_obs, counts_obs, yerr=err, fmt='o')
axis[1].set(xlabel='t [s]', ylabel='N')
plt.tight_layout()
plt.savefig("E2_Problem_1.pdf")
plt.clf()

# Problema 2: PDF Exponencial Teórica
def decay_pdf(t_val, tau):
    return (1.0 / tau) * np.exp(-1.0 * t_val / tau)

x_p2 = np.linspace(0.0, 10.0, 1000)
f1 = decay_pdf(x_p2, 1.0)
f2 = decay_pdf(x_p2, 2.0)
f3 = decay_pdf(x_p2, 0.5)

plt.plot(x_p2, f1, label=r"$\tau = 1.0$ s")
plt.plot(x_p2, f2, label=r"$\tau = 2.0$ s")
plt.plot(x_p2, f3, label=r"$\tau = 0.5$ s")
plt.xlabel('t [s]')
plt.ylabel('f(t; τ)')
plt.legend(loc="upper right")
plt.savefig("E2_Problem_2.pdf")
plt.clf()

prob_p2 = integrate.quad(lambda val: decay_pdf(val, 2.0), 0.0, 1.0)[0]
print(f"P(t <= 1s | tau=2.0) = {prob_p2 * 100:.2f}%")

# Problema 3: Verossimilhança para medida única (N=1, t=1)
def Likelihood(tau, N, sum_t):
    return ((1.0 / tau) ** N) * np.exp(-sum_t / tau)

x_p3 = np.linspace(0.5, 1.5, 1000)
L1 = Likelihood(x_p3, 1, 1.0)

plt.plot(x_p3, L1)
plt.xlabel(r'$\tau$ [s]')
plt.ylabel(r'$L(\tau)$')
plt.savefig("E2_Problem_3.pdf")
plt.clf()

# Problemas 4 e 5: Ajuste de Máxima Verossimilhança Não Binado (-2 ln L)
def lnL(tau, N, sum_t):
    return 2.0 * N * np.log(tau) + 2.0 * sum_t / tau

N_obs = len(t)
sum_t_obs = sum(t)
tau_hat = sum_t_obs / N_obs
sigma_approx = tau_hat / np.sqrt(N_obs)

x_p4 = np.linspace(max(0.1, tau_hat - 5 * sigma_approx), tau_hat + 5 * sigma_approx, 2000)
logLikelihood = lnL(x_p4, N_obs, sum_t_obs)

plt.plot(x_p4, logLikelihood)
plt.xlabel(r'$\tau$ [s]')
plt.ylabel(r'$-2 \ln L(\tau)$')
plt.savefig("E2_Problem_4.pdf")
plt.clf()

print(f"Estimador de maxima verossimilhanca (tau_hat): {tau_hat:.4f} s")

min_lnL_val = lnL(tau_hat, N_obs, sum_t_obs)

def moved_lnL(tau_val):
    return lnL(tau_val, N_obs, sum_t_obs) - (min_lnL_val + 1.0)

sigma_down = tau_hat - brentq(moved_lnL, max(0.01, tau_hat - 3 * sigma_approx), tau_hat)
sigma_up = brentq(moved_lnL, tau_hat, tau_hat + 3 * sigma_approx) - tau_hat

print(f"Incerteza +sigma: {sigma_up:.4f}")
print(f"Incerteza -sigma: {sigma_down:.4f}")

# Problema 6: Distribuição Gaussiana
def Gaussian(x_val, mu, sigma):
    return (1.0 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x_val - mu) ** 2) / (2 * sigma ** 2))

x_p6 = np.linspace(-5, 5, 1000)
g1 = Gaussian(x_p6, 0.0, 1.0)
g2 = Gaussian(x_p6, 1.0, 1.0)
g3 = Gaussian(x_p6, 0.0, 2.0)

plt.plot(x_p6, g1, label=r"$\mu=0, \sigma=1$")
plt.plot(x_p6, g2, label=r"$\mu=1, \sigma=1$")
plt.plot(x_p6, g3, label=r"$\mu=0, \sigma=2$")
plt.legend(loc="upper left")
plt.xlabel("x")
plt.ylabel("P(x)")
plt.savefig('E1_Problem_1.pdf')
plt.clf()

p_205 = integrate.quad(lambda val: Gaussian(val, 200.0, 2.0), 205.0, np.inf)[0]
p_203_single = integrate.quad(lambda val: Gaussian(val, 200.0, 2.0), 203.0, np.inf)[0]
p_203_double = p_203_single ** 2

print(f"P(m >= 205 GeV): {p_205 * 100:.2f}%")
print(f"P(duas particulas com m >= 203 GeV): {p_203_double * 100:.2f}%")

# Problema 7: Teorema Central do Limite (TCL)
x_histo_3, x_histo_30, x_histo_60, x_histo_100 = [], [], [], []

for i in range(10000):
    for N_val, histo in zip([3, 30, 60, 100], [x_histo_3, x_histo_30, x_histo_60, x_histo_100]):
        x_sum = sum(np.random.exponential(scale=j + 1.0) for j in range(N_val))
        histo.append(x_sum / N_val)

fig, axis = plt.subplots(2, 2, constrained_layout=True)
axis[0, 0].hist(x_histo_3, bins=20)
axis[0, 0].set_title("N = 3")
axis[0, 0].set_xlabel("x")

axis[0, 1].hist(x_histo_30, bins=20)
axis[0, 1].set_title("N = 30")
axis[0, 1].set_xlabel("x")

axis[1, 0].hist(x_histo_60, bins=20)
axis[1, 0].set_title("N = 60")
axis[1, 0].set_xlabel("x")

axis[1, 1].hist(x_histo_100, bins=20)
axis[1, 1].set_title("N = 100")
axis[1, 1].set_xlabel("x")

plt.savefig('E1_Problem_2.pdf')
plt.clf()
plt.savefig("E2_Problem_4.pdf")
plt.clf()

print(f"Estimador de maxima verossimilhanca (tau_hat): {tau_hat:.4f} s")

min_lnL_val = lnL(tau_hat, N_obs, sum_t_obs)

def moved_lnL(tau_val):
    return lnL(tau_val, N_obs, sum_t_obs) - (min_lnL_val + 1.0)

# Procura das incertezas garantindo um intervalo positivo
sigma_down = tau_hat - brentq(moved_lnL, max(0.01, tau_hat - 0.5), tau_hat)
sigma_up = brentq(moved_lnL, tau_hat, tau_hat + 0.5) - tau_hat

print(f"Incerteza +sigma: {sigma_up:.4f}")
print(f"Incerteza -sigma: {sigma_down:.4f}")
# Procura das incertezas garantindo um intervalo positivo
sigma_down = tau_hat - brentq(moved_lnL, max(0.01, tau_hat - 0.5), tau_hat)
sigma_up = brentq(moved_lnL, tau_hat, tau_hat + 0.5) - tau_hat

print(f"Incerteza +sigma: {sigma_up:.4f}")
print(f"Incerteza -sigma: {sigma_down:.4f}")
# Limites dinamicos para encontrar o cruzamento da incerteza (+1 unidade em -2lnL)
sigma_down = tau_hat - brentq(moved_lnL, tau_hat - 1.0, tau_hat)
sigma_up = brentq(moved_lnL, tau_hat, tau_hat + 1.0) - tau_hat
print(f"Incerteza +sigma: {sigma_up:.4f}")
print(f"Incerteza -sigma: {sigma_down:.4f}")
# Problema 6: Distribuição Gaussiana e Física de Partículas
def Gaussian(x_val, mu, sigma):
    return (1.0 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x_val - mu) ** 2) / (2 * sigma ** 2))

x_p6 = np.linspace(-5, 5, 1000)
g1 = Gaussian(x_p6, 0.0, 1.0)
g2 = Gaussian(x_p6, 1.0, 1.0)
g3 = Gaussian(x_p6, 0.0, 2.0)

plt.plot(x_p6, g1, label=r"$\mu=0, \sigma=1$")
plt.plot(x_p6, g2, label=r"$\mu=1, \sigma=1$")
plt.plot(x_p6, g3, label=r"$\mu=0, \sigma=2$")
plt.legend(loc="upper left")
plt.xlabel("x")
plt.ylabel("P(x)")
plt.savefig('E1_Problem_1.pdf')
plt.clf()

p_205 = integrate.quad(lambda val: Gaussian(val, 200.0, 2.0), 205.0, np.inf)[0]
p_203_single = integrate.quad(lambda val: Gaussian(val, 200.0, 2.0), 203.0, np.inf)[0]
p_203_double = p_203_single ** 2

print(f"P(m >= 205 GeV): {p_205 * 100:.2f}%")
print(f"P(duas particulas com m >= 203 GeV): {p_203_double * 100:.2f}%")

# Problema 7: Teorema Central do Limite (TCL)
x_histo_3, x_histo_30, x_histo_60, x_histo_100 = [], [], [], []

for i in range(10000):
    for N_val, histo in zip([3, 30, 60, 100], [x_histo_3, x_histo_30, x_histo_60, x_histo_100]):
        x_sum = sum(np.random.exponential(scale=j + 1.0) for j in range(N_val))
        histo.append(x_sum / N_val)

fig, axis = plt.subplots(2, 2, constrained_layout=True)
axis[0, 0].hist(x_histo_3, bins=20)
axis[0, 0].set_title("N = 3")
axis[0, 0].set_xlabel("x")

axis[0, 1].hist(x_histo_30, bins=20)
axis[0, 1].set_title("N = 30")
axis[0, 1].set_xlabel("x")

axis[1, 0].hist(x_histo_60, bins=20)
axis[1, 0].set_title("N = 60")
axis[1, 0].set_xlabel("x")

axis[1, 1].hist(x_histo_100, bins=20)
axis[1, 1].set_title("N = 100")
axis[1, 1].set_xlabel("x")

plt.savefig('E1_Problem_2.pdf')
plt.clf()
