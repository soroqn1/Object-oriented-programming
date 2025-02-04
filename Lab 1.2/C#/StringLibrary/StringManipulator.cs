using System;

namespace StringLibrary
{
    public class StringManipulator
    {
        private string text;

        public StringManipulator()
        {
            text = "";
        }

        public StringManipulator(string input)
        {
            text = input.ToUpper();
        }

        public StringManipulator(StringManipulator other) : this(other.text) {}

        public string Text => text;

        public int GetLength(bool ignoreSpaces = false)
        {
            return ignoreSpaces ? text.Replace(" ", "").Length : text.Length;
        }

        public void ReplaceChar(char oldChar, char newChar)
        {
            text = text.Replace(char.ToUpper(oldChar), char.ToUpper(newChar))
                       .Replace(char.ToLower(oldChar), char.ToLower(newChar));
        }
    }
}