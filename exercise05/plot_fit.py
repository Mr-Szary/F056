import ROOT

file = ROOT.TFile("dados.root", "READ")
tree = file.Get("tree")

# histograma
h = ROOT.TH1F("h", "Distri. Gerada; Valor gerado; N. Entradas", 50, -5, 5)
for event in tree:
    h.Fill(event.x)
h.SetLineColor(ROOT.kBlack)
h.SetLineStyle(1)
h.SetLineWidth(3)
h.SetFillColor(ROOT.kYellow)

#canvas
c = ROOT.TCanvas("c", "Histograma", 800, 600)
c.SetFillColor(ROOT.kWhite)

#fit
h.Fit("gaus")
h.Draw()

c.SaveAs("hist_py.png")
file.Close()
