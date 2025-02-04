using System;
using StringLibrary; // Підключаємо бібліотеку

class Program
{
    static void Main()
    {
        // Використання всіх конструкторів
        StringManipulator str1 = new StringManipulator();
        StringManipulator str2 = new StringManipulator("Hello World");
        StringManipulator str3 = new StringManipulator(str2);

        Console.WriteLine($"Рядок 1: \"{str1.Text}\", Довжина (з пробілами): {str1.GetLength()}, Без пробілів: {str1.GetLength(true)}");
        Console.WriteLine($"Рядок 2: \"{str2.Text}\", Довжина (з пробілами): {str2.GetLength()}, Без пробілів: {str2.GetLength(true)}");
        Console.WriteLine($"Рядок 3 (копія): \"{str3.Text}\", Довжина (з пробілами): {str3.GetLength()}, Без пробілів: {str3.GetLength(true)}");

        // Тест заміни символів
        str2.ReplaceChar('O', 'A');
        Console.WriteLine($"Рядок 2 після заміни: \"{str2.Text}\"");
    }

    // Деструктор
    ~Program()
    {
        // Код для виконання при знищенні об'єкта
        Console.WriteLine("Program object is being destroyed");
    }
}