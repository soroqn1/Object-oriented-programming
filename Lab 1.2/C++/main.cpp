#include "Strings.h"
#include <iostream>

int main() {
    char initialString[100];
    char oldChar, newChar;

    std::cout << "Enter a string: ";
    std::cin.getline(initialString, 100);

    Strings myString(initialString);

    std::cout << "String value: " << myString.getStringValue() << std::endl;
    std::cout << "String length: " << myString.calculateLength() << std::endl;

    std::cout << "Enter the character to replace: ";
    std::cin >> oldChar;
    std::cout << "Enter the new character: ";
    std::cin >> newChar;

    myString.replaceChar(oldChar, newChar);

    std::cout << "Modified string value: " << myString.getStringValue() << std::endl;

    return 0;
}
