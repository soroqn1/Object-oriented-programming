#include <iostream>
#include "StringManipulator.h"

int main() {
    // Використання всіх конструкторів
    StringManipulator str1;
    StringManipulator str2("Hello World");
    StringManipulator str3(str2);
    StringManipulator str4(std::move(str2));

    std::cout << "Рядок 1: " << str1.GetText() << ", Довжина: " << str1.GetLength() << std::endl;
    std::cout << "Рядок 2: " << str2.GetText() << ", Довжина: " << str2.GetLength() << std::endl;
    std::cout << "Рядок 3 (копія): " << str3.GetText() << ", Довжина: " << str3.GetLength() << std::endl;
    std::cout << "Рядок 4 (переміщений): " << str4.GetText() << ", Довжина: " << str4.GetLength() << std::endl;

    // Заміна символів
    str3.ReplaceChar('O', 'A');
    std::cout << "Рядок 3 після заміни: " << str3.GetText() << std::endl;

    return 0;
}
