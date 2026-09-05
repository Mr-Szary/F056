void generate() {
    //Parâmetros iniciais
    const int N = 1000;
    double mean = 0.0;
    double sigma = 1.0;
 
    TFile *file = new TFile("dados.root", "RECREATE");
    
    //TTree e branch
    TTree *tree = new TTree("tree", "Numeros random gauss");
    double x;
    tree->Branch("x", &x, "x/D");

    TRandom3 rnd(0); 
    for (int i = 0; i < N; i++) {
        x = rnd.Gaus(mean, sigma); // média 0 e des.padr 
        tree->Fill();             
    }

    file->cd();
    tree->Write();
    file->Close();
}
