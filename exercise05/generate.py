import ROOT


#Parâmetros
N = 1000
mean = 0.0
sigma = 1.0

#TFile
file = ROOT.TFile("dados.root", "RECREATE")

#TTree e branch
import array
tree = ROOT.TTree("tree", "Numeros random gauss")
x = array.array('d', [0.0]) 
tree.Branch("x", x, "x/D")

#Random
rand = ROOT.TRandom3(0)
for i in range(N):
    x[0] = rand.Gaus(mean, sigma)
    tree.Fill()

file.cd()
tree.Write()
file.Close()
