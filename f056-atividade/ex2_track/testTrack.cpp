#include <iostream>
#include "SimTrack.h"

int main() {
    SimTrack trackNormal(50.0, 30.0, 40.0, 0.0, 11, 23);
    
    SimTrack trackLimite(100.0, 0.0, 0.0, 99.0, 211, 24);

    std::cout << "--- Traco Normal ---\n";
    std::cout << "pT: " << trackNormal.Pt() << "\n";
    std::cout << "Eta: " << trackNormal.Eta() << "\n";
    std::cout << "ID da Particula: " << trackNormal.ParticleId() << "\n";
    std::cout << "ID da Particula-Mae: " << trackNormal.ParentId() << "\n\n";


    std::cout << "--- Traco Limite (pT = 0) ---\n";
    std::cout << "pT: " << trackLimite.Pt() << "\n";
    std::cout << "Eta: " << trackLimite.Eta() << " (Deve ser um valor limite seguro, sem erro matemático)\n";
    std::cout << "ID da Particula: " << trackLimite.ParticleId() << "\n";
    std::cout << "ID da Particula-Pai: " << trackLimite.ParentId() << "\n";

    return 0;
}
