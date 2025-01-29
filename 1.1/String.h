#ifndef STRINGCLASS_H
#define STRINGCLASS_H

#include <string>

class StringClass {
private:
    std::string value;
public:
    StringClass(const std::string& str);
    int length() const;
    void replace(char oldChar, char newChar);
    std::string getValue() const;
};

#endif // STRINGCLASS_H
