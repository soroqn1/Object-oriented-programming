using System;
using String_manipulator;

public class Program {
    static void Main()
    {
        Console.Write("Type string: ");
        string input = Console.ReadLine() ?? "";
        
        Console.WriteLine("Old symbol to replace:");
        string oldletter = Console.ReadLine() ?? "";

        Console.WriteLine("New symbol to replace:");
        string newletter = Console.ReadLine() ?? "";

        Strings stringManipulator = new Strings();
        stringManipulator.Main(input, oldletter, newletter);
    }
}