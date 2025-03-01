using System;

public class String {

    static void Main(string input, string oldletter, string newletter)  
    {
        Console.WriteLine("Input: " + input);
        Console.WriteLine("Uppercase: " + input.ToUpper());
        Console.WriteLine("Length: " + input.Length);
        Console.WriteLine("Replace: " + input.Replace(oldletter, newletter));
    }
}   