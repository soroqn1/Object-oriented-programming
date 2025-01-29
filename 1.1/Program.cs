using System;

class Program {
    static void Main() {
        Console.Write("Enter a string: ");
        string input = Console.ReadLine();

        StringClass myString = new StringClass(input);
        Console.WriteLine("Original string: " + myString.GetValue());
        Console.WriteLine("Length: " + myString.GetLength());

        Console.Write("Enter character to replace: ");
        char oldChar = Console.ReadKey().KeyChar;
        Console.WriteLine();

        Console.Write("Enter new character: ");
        char newChar = Console.ReadKey().KeyChar;
        Console.WriteLine();

        myString.ReplaceChar(oldChar, newChar);
        Console.WriteLine("Modified string: " + myString.GetValue());
    }
}
