#include "String.h"

int main() {
    std::string input, oldLetter, newLetter;

    std::cout << "Type string: ";
    std::getline(std::cin, input);

    std::cout << "Old symbol to replace: ";
    std::getline(std::cin, oldLetter);

    std::cout << "New symbol to replace: ";
    std::getline(std::cin, newLetter);

    MainClass transfer;
    transfer.processString(input, oldLetter, newLetter);

    return 0;
}
