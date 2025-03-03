using System;
using String_manipulator;

namespace Console_application {

public class Program {
    public static void Main(string[] args)
    {
        Program program = new Program();
        program.Input();
    }

    public void Input()
    {
        Console.Write("Type string: ");
        string input = Console.ReadLine() ?? "";
        
        Console.WriteLine("Old symbol to replace:");
        string oldletter = Console.ReadLine() ?? "";

        Console.WriteLine("New symbol to replace:");
        string newletter = Console.ReadLine() ?? "";

        MainClass transfer = new MainClass();
        transfer.Main(input, oldletter, newletter);
    }

    public void Output(string input, int input_Length, string input_Uppercase, string input_Replace)
    {
        Console.WriteLine("");
        Console.WriteLine("Input: " + input);
        Console.WriteLine("Uppercase: " + input_Uppercase);
        Console.WriteLine("Length: " + input_Length);
        Console.WriteLine("Replace: " + input_Replace);
    }
  }
}