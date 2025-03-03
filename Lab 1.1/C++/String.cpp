#include "String.h"
#include <iostream>
#include <string>

class StringManipulator {
public:
void Main(const std::string& input, const std::string& oldLetter, const std::string& newLetter) {

    std::cout << "Input: " << input << std::endl;
    
    std::string Uppercase_input = input;
    for (char &c : Uppercase_input) c = std::toupper(c);
    std::cout << "Uppercase: " << Uppercase_input << std::endl;

    std::cout << "Length: " << input.length() << std::endl;

    std::string replaced_input = input;
    std::replace(replaced_input.begin(), replaced_input.end(), oldLetter, newLetter);
    std::cout << "Replace: " << replaced_input << std::endl;

    }
};