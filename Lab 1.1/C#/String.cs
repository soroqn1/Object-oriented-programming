using System;

namespace String_manipulator {

public class MainClass {
    public void Main(string input, string oldletter, string newletter)  
    {
        Console.WriteLine("");
        Console.WriteLine("Input: " + input);
        Console.WriteLine("Uppercase: " + input.ToUpper());
        Console.WriteLine("Length: " + input.Length);
        Console.WriteLine("Replace: " + input.Replace(oldletter, newletter));
    }
  }
}   