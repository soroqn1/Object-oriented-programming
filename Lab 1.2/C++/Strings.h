#ifndef STRINGS_H
#define STRINGS_H

class Strings {
private:
    char* value;
public:
    Strings(const char* initialValue);
    ~Strings();
    int calculateLength() const;
    void replaceChar(char oldChar, char newChar);
    const char* getStringValue() const;
};

#endif // STRINGS_H
