#include "Strings.h"
#include <cstring>
#include <iostream>

Strings::Strings(const char* initialValue) {
    value = new char[strlen(initialValue) + 1];
    strcpy(value, initialValue);
}

Strings::~Strings() {
    delete[] value;
}

int Strings::calculateLength() const {
    return strlen(value);
}

void Strings::replaceChar(char oldChar, char newChar) {
    for (int i = 0; i < strlen(value); ++i) {
        if (value[i] == oldChar) {
            value[i] = newChar;
        }
    }
}

const char* Strings::getStringValue() const {
    return value;
}
