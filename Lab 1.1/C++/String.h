#ifndef STRING_H
#define STRING_H

#include <string>

class StringManipulator {
public:
    std::string toUppercase(std::string input);
    std::string replaceLetters(std::string input, char oldLetter, char newLetter);
    size_t getLength(std::string input);
};

#endif