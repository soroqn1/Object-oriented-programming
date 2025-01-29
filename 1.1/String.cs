using System;

public class StringClass {
    private string value;

    public StringClass(string str) {
        value = str.ToUpper();
    }

    public int GetLength() {
        return value.Length;
    }

    public void ReplaceChar(char oldChar, char newChar) {
        value = value.Replace(char.ToUpper(oldChar), char.ToUpper(newChar));
    }

    public string GetValue() {
        return value;
    }
}
