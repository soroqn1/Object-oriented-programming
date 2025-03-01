using System;

public class Program {
    public static void Main1(string[] args)
    {
        Console.Write("Type string: ");
        Console.WriteLine("Old symbol to replace:");
        string oldletter = Console.ReadLine() ?? "";

        Console.WriteLine("New symbol to replace:");
        string newletter = Console.ReadLine() ?? "";
    }
}