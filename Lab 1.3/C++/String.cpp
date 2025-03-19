#include <algorithm>
#include "String.h"

StringManipulator::StringManipulator() : input(""), oldLetter('\0'), newLetter('\0') {}

StringManipulator::StringManipulator(std::string input, char oldLetter, char newLetter) 
    : input(input), oldLetter(oldLetter), newLetter(newLetter) {}

StringManipulator::StringManipulator(const StringManipulator& other) 
    : input(other.input), oldLetter(other.oldLetter), newLetter(other.newLetter) {}

StringManipulator::~StringManipulator() {}

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

std::string StringManipulator::getString() const {
    return input;
}

StringManipulator StringManipulator::operator+(const StringManipulator &other) const {
    StringManipulator result(*this);
    result.input += other.input;
    return result;
}

StringManipulator StringManipulator::operator-(char c) const {
    StringManipulator result(*this);
    result.input.erase(
        std::remove(result.input.begin(), result.input.end(), c),
        result.input.end()
    );
    return result;
}

StringManipulator StringManipulator::combineAndRemoveZero(const StringManipulator &s2, const StringManipulator &s3) {
    StringManipulator s3Modified = s3 - '0';
    return s2 + s3Modified;
}