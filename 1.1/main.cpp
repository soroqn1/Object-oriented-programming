#include <iostream>
#include "String.h"

int main() {
    std::string input;
    std::cout << "Enter a string: ";
    std::cin >> input;

    StringClass myString(input);
    std::cout << "Original string: " << myString.getValue() << std::endl;
    std::cout << "Length: " << myString.length() << std::endl;

    char oldChar, newChar;
    std::cout << "Enter character to replace: ";
    std::cin >> oldChar;
    std::cout << "Enter new character: ";
    std::cin >> newChar;

    myString.replace(oldChar, newChar);
    std::cout << "Modified string: " << myString.getValue() << std::endl;

    return 0;
}
