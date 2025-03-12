#include <algorithm>
#include "String.h"

std::string StringManipulator::toUppercase(std::string input) 
{
    for (char &c : input) c = std::toupper(c);
    return input;
}

std::string StringManipulator::replaceLetters(std::string input, char oldLetter, char newLetter) 
{
    std::replace(input.begin(), input.end(), oldLetter, newLetter);
    return input;
}

size_t StringManipulator::getLength(std::string input) 
{
    return input.length();
}