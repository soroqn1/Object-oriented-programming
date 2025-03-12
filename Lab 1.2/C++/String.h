#ifndef STRING_H
#define STRING_H

#include <string>

class StringManipulator {
private:
    std::string input;
    char oldLetter;
    char newLetter;

public:
    StringManipulator();

    StringManipulator(std::string input, char oldLetter, char newLetter);

    StringManipulator(const StringManipulator& other);

    ~StringManipulator();

    std::string toUppercase(std::string input);
    std::string replaceLetters(std::string input, char oldLetter, char newLetter);
    size_t getLength(std::string input);
};

#endif