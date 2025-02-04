#ifndef STRINGMANIPULATOR_H
#define STRINGMANIPULATOR_H

#include <string>

class StringManipulator {
private:
    std::string text; // Закрите поле

public:
    // Конструктори
    StringManipulator();
    StringManipulator(const std::string& input);
    StringManipulator(const StringManipulator& other); // Конструктор копіювання
    StringManipulator(StringManipulator&& other) noexcept; // Конструктор переміщення
    ~StringManipulator();

    // Гетери
    std::string GetText() const;
    size_t GetLength() const;

    // Метод заміни символів
    void ReplaceChar(char oldChar, char newChar);
};

#endif
