#include <iostream>
#include <string>
#include "String.h"

int main() {
    std::string input;
    char oldLetter, newLetter;

    std::cout << "Type string: ";
    std::getline(std::cin, input);

    std::cout << "Old symbol to replace: ";
    std::cin >> oldLetter;

    std::cout << "New symbol to replace: ";
    std::cin >> newLetter;

    StringManipulator transfer;

    std::cout << "Input: " << input << std::endl;
    std::cout << "Uppercase: " << transfer.toUppercase(input) << std::endl;
    std::cout << "Length: " << transfer.getLength(input) << std::endl;
    std::cout << "Replace: " << transfer.replaceLetters(input, oldLetter, newLetter) << std::endl;

    return 0;
}
