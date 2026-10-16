#include "Pythia8/Pythia.h"
using namespace Pythia8;

int main() {
    Pythia pythia;
    
    // Configuracao do feixe
    pythia.readString("Beams:eCM = 13000."); // 13 TeV
    
    // Ativa o processo qqbar -> ttbar
    pythia.readString("Top:qqbar2ttbar = on");
    // Ativa o processo gg -> ttbar.
    pythia.readString("Top:gg2ttbar = on");
    
    // Inicializacao
    pythia.init();
    
    int nEvents = 10000;
    for (int iEvent = 0; iEvent < nEvents; ++iEvent) {
        if (!pythia.next()) continue;
    }
    
    pythia.stat();
    
    // Imprime sigmaGen() e sigmaErr() explicitamente em picobarns (pb)
    cout << "sigma = " << pythia.info.sigmaGen() * 1e9 << " +- "
         << pythia.info.sigmaErr() * 1e9 << " pb" << endl;
         
    return 0;
}
