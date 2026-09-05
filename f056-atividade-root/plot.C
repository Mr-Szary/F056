void plot() {
    TFile *file = new TFile("dados.root", "READ");
    TTree *tree = (TTree*) file->Get("tree");

    double x;
    tree->SetBranchAddress("x", &x);

    TH1F *h = new TH1F("h", "Distri. Gerada; Valor gerado; N. Entradas", 50, -5, 5);

    Long64_t nentries = tree->GetEntries();
    for (Long64_t i = 0; i < nentries; i++) {
        tree->GetEntry(i);
        h->Fill(x);
    }

    h->SetLineColor(kBlack);
    h->SetLineStyle(1);
    h->SetLineWidth(3);
    h->SetFillColor(kYellow);

    TCanvas *c = new TCanvas("c", "Histograma", 800, 600);
    c->SetFillColor(kWhite);

    h->Fit("gaus");
    h->Draw();

    c->SaveAs("hist.png");
    file->Close();
}
