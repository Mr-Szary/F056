#include <iostream>
#include <string>


using namespace std;
int main(int argc, char* argv[]) {
    if (argc < 2){
        std::cout << "Digite um número por gentileza" << std::endl;
    return 1;}

    double num = std::stod(argv[1]);
    std::cout << "Hello World " << num << std::endl;
    return 0;
}

