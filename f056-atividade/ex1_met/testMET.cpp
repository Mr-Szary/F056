#include <iostream>
#include "SimpleMET.h"

int main() {
    SimpleMET met;
    met.Add(50.0, 20.0);
    met.Add(-50.0, -20.0);
    
    std::cout << "MET Value: " << met.Value() << "\n";
    std::cout << "MET Phi: " << met.Phi() << "\n";
    return 0;
}
