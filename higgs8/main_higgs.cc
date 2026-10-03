#include "Pythia8/Pythia.h"
#include "TFile.h"
#include "TTree.h"
#include "TH1F.h"
#include <iostream>

using namespace Pythia8;

int main() {
    Pythia pythia;
    
    // ---------------------------------------------------------
    // ATENÇÃO: Altere os nomes aqui para cada simulação!
    pythia.readFile("bg_zjatos.cmnd"); 
    TFile* file = new TFile("bg_zjatos.root", "RECREATE");
    // ---------------------------------------------------------
    
    pythia.init();
    
    TTree* tree = new TTree("events", "Arvore de Eventos");
    double mH;
    tree->Branch("mH", &mH, "mH/D");

    int nEvents = pythia.mode("Main:numberOfEvents");

    for (int iEvent = 0; iEvent < nEvents; ++iEvent) {
        if (!pythia.next()) continue;

        Vec4 pH(0., 0., 0., 0.);
        int nB = 0;
        for (int i = 0; i < pythia.event.size(); ++i) {
            if (abs(pythia.event[i].id()) == 5) {
                int moth = pythia.event[i].mother1();
                if (moth > 0 && pythia.event[moth].id() == 25) {
                    pH += pythia.event[i].p();
                    nB++;
                }
            }
        }

        if (nB < 2) {
            pH = Vec4(0., 0., 0., 0.);
            int ib1 = -1, ib2 = -1;
            double pt1 = -1., pt2 = -1.;

            for (int i = 0; i < pythia.event.size(); ++i) {
                if (abs(pythia.event[i].id()) == 5) {
                    double pt = pythia.event[i].pT();
                    if (pt > pt1) {
                        pt2 = pt1; ib2 = ib1;
                        pt1 = pt;  ib1 = i;
                    } else if (pt > pt2) {
                        pt2 = pt;  ib2 = i;
                    }
                }
            }

            if (ib1 >= 0 && ib2 >= 0) {
                pH = pythia.event[ib1].p() + pythia.event[ib2].p();
                nB = 2; 
            }
        }

        if (nB == 2) {
            mH = pH.mCalc();
            tree->Fill();
        }
    }

    pythia.stat();
    tree->Write();
    file->Close();
    delete file;

    return 0;
}
