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
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    StringManipulator transfer;

    std::cout << "Input: " << input << std::endl;
    std::cout << "Uppercase: " << transfer.toUppercase(input) << std::endl;
    std::cout << "Length: " << transfer.getLength(input) << std::endl;
    std::cout << "Replace: " << transfer.replaceLetters(input, oldLetter, newLetter) << std::endl;

    StringManipulator CS1;

    std::string input2;
    std::cout << "Enter string for CS2: ";
    std::getline(std::cin, input2);
    StringManipulator CS2(input2, '\0', '\0');

    std::string input3;
    std::cout << "Enter string for CS3: ";
    std::getline(std::cin, input3);
    StringManipulator CS3(input3, '\0', '\0');

    CS1 = transfer.combineAndRemoveZero(CS2, CS3);

    std::cout << "CS1: " << CS1.getString() << std::endl;

    return 0;
}
