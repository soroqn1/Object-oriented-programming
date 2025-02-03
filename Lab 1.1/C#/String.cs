using System;

public class StringClass {
    private string value;

    public StringClass(string str) {
        value = str.ToUpper(); 
    }

    public int GetLength() {
        return value.Replace(" ", "").Length; 
    }

    public string GetValue() {
        return value;
    }

    public void ReplaceChar(char oldChar, char newChar) {
        value = value.Replace(oldChar, newChar);
    }
}
