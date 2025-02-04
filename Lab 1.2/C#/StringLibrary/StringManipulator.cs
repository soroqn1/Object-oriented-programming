using System;

namespace StringLibrary
{
    public class StringManipulator
    {
        private string text;  // Приватне поле

        // Конструктор за замовчуванням
        public StringManipulator()
        {
            text = "";
        }

        // Конструктор із параметром
        public StringManipulator(string input)
        {
            text = input.ToUpper();
        }

        // Конструктор копіювання
        public StringManipulator(StringManipulator other) : this(other.text) {}

        // Властивість (читання значення)
        public string Text => text;

        // Метод обчислення довжини рядка (без урахування пробілів)
        public int GetLength(bool ignoreSpaces = false)
        {
            return ignoreSpaces ? text.Replace(" ", "").Length : text.Length;
        }

        // Метод заміни символа (нечутливий до регістру)
        public void ReplaceChar(char oldChar, char newChar)
        {
            text = text.Replace(char.ToUpper(oldChar), char.ToUpper(newChar))
                       .Replace(char.ToLower(oldChar), char.ToLower(newChar));
        }
    }
}