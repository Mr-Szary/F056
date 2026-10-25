import numpy as np
import matplotlib.pyplot as plt
from iminuit import Minuit
from scipy.stats import chi2
import uproot
import os

# Garante que o diretório para as figuras exista
os.makedirs('figuras', exist_ok=True)

# Parâmetros gerais
MMIN = 50.0
MMAX = 400.0

# Funções do modelo
def fs(m, mu, sigma):
    return (1.0 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * ((m - mu) / sigma)**2)

def fbw(m, mu_bw, bw_gamma):
    return (2 / np.pi) * bw_gamma / (4 * (m - mu_bw)**2 + bw_gamma**2)

def fexp(m, tau, m_min=MMIN):
    return (1.0 / tau) * np.exp(-(m - m_min) / tau)

def previsao_modelo(centros, mu, sigma, mu_bw, bw_gamma, tau, s, b_bw, b_exp, largura_bin):
    sinal = fs(centros, mu, sigma)
    back_bw = fbw(centros, mu_bw, bw_gamma)
    back_exp = fexp(centros, tau)
    densidade = s * sinal + b_bw * back_bw + b_exp * back_exp
    return densidade * largura_bin

# Extração de dados reais do ficheiro ROOT
ficheiro = uproot.open("pythia_higgs.root")
dados_mH = ficheiro["events"]["mH"].array(library="np")
n_total = len(dados_mH)

# Estudo de dependência do número de bins
lista_nbins = [50, 100, 200, 500, 1000]
resultados_mu = []
resultados_sigma = []
resultados_s = []

for nbins in lista_nbins:
    largura_bin = (MMAX - MMIN) / nbins
    
    # Histograma com os dados reais
    contagens, bordas = np.histogram(dados_mH, bins=nbins, range=(MMIN, MMAX))
    centros_bins = (bordas[:-1] + bordas[1:]) / 2.0

    def chi2_fit(mu, sigma, mu_bw, bw_gamma, tau, s, b_bw, b_exp):
        previsao = previsao_modelo(centros_bins, mu, sigma, mu_bw, bw_gamma, tau, s, b_bw, b_exp, largura_bin)
        
        # Correção da variância usando a previsão do modelo
        variancia = np.maximum(previsao, 1.e-3)
        residuos = contagens - previsao
        return np.sum(residuos**2 / variancia)

    # Inicialização proporcional baseada no n_total
    fit = Minuit(chi2_fit, 
                 mu=125.0, sigma=4.0, 
                 mu_bw=91.0, bw_gamma=5.0, 
                 tau=50.0, 
                 s=0.27 * n_total, b_bw=0.30 * n_total, b_exp=0.43 * n_total)

    fit.limits["sigma"] = (1.e-4, 50.0)
    fit.errordef = Minuit.LEAST_SQUARES

    fit.migrad()
    fit.hesse()

    # Validação e extração de resultados
    if not fit.valid:
        print(f"[NBINS={nbins}] Aviso: O ajuste não convergiu.")
        
    chi2_val = fit.fval
    ndof = len(contagens) - fit.nfit
    p_value = chi2.sf(chi2_val, ndof)
    
    print(f"\n--- Ajuste com {nbins} Bins ---")
    print(f"Chi2 / ndof: {chi2_val:.2f} / {ndof} = {chi2_val/ndof:.3f}")
    print(f"P-valor: {p_value:.4e}")
    print(f"mu = {fit.values['mu']:.2f} +/- {fit.errors['mu']:.2f}")
    
    resultados_mu.append(fit.values['mu'])
    resultados_sigma.append(fit.values['sigma'])
    resultados_s.append(fit.values['s'])

# Geração de gráfico da dependência
plt.plot(lista_nbins, resultados_mu, marker='o', color='blue')
plt.xlabel('Número de Bins')
plt.ylabel(r'Massa $\mu$ ajustada (GeV)')
plt.title(r'Dependência do parâmetro $\mu$ com NBINS')
plt.grid(True)
plt.savefig('figuras/ajuste_melhorado_nbins.png')
plt.clf()
