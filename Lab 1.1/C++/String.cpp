#include "String.h"
#include <algorithm>
#include <cctype>

StringClass::StringClass(const std::string& str) {
    value = str;
}

int StringClass::length() const {
    return value.length();
}

void StringClass::replace(char oldChar, char newChar) {
    oldChar = std::toupper(oldChar);
    newChar = std::toupper(newChar);
    std::replace(value.begin(), value.end(), oldChar, newChar);
}

std::string StringClass::getValue() const {
    return value;
}
