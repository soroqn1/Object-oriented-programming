#include "StringManipulator.h"
#include <algorithm>

// Конструктор за замовчуванням
StringManipulator::StringManipulator() : text("") {}

// Конструктор із параметром
StringManipulator::StringManipulator(const std::string& input) {
    text = input;
    std::transform(text.begin(), text.end(), text.begin(), ::toupper);
}

// Конструктор копіювання
StringManipulator::StringManipulator(const StringManipulator& other) {
    text = other.text;
}

// Конструктор переміщення
StringManipulator::StringManipulator(StringManipulator&& other) noexcept {
    text = std::move(other.text);
}

// Деструктор
StringManipulator::~StringManipulator() {}

// Гетери
std::string StringManipulator::GetText() const {
    return text;
}

size_t StringManipulator::GetLength() const {
    return text.length();
}

// Метод заміни символа
void StringManipulator::ReplaceChar(char oldChar, char newChar) {
    std::replace(text.begin(), text.end(), oldChar, newChar);
}
