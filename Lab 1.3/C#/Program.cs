using System;
using String_manipulator;

namespace Chip {

public class Program {

    public static void Main(string[] args)
    {
        Console.Write("(CS2)Type string: ");
        string inputCS2 = Console.ReadLine() ?? "";
        Console.WriteLine("(CS2)Old symbol to replace:");
        string oldletterCS2 = Console.ReadLine() ?? "";
        Console.WriteLine("(CS2)New symbol to replace:");
        string newletterCS2 = Console.ReadLine() ?? "";

        Console.Write("(CS3)Type string: ");
        string inputCS3 = Console.ReadLine() ?? "";
        Console.WriteLine("(CS3)Old symbol to replace:");
        string oldletterCS3 = Console.ReadLine() ?? "";
        Console.WriteLine("(CS3)New symbol to replace:");
        string newletterCS3 = Console.ReadLine() ?? "";

        Processing transfer = new Processing();
        transfer.Manipulator(inputCS2, oldletterCS2, newletterCS2, inputCS3, oldletterCS3, newletterCS3);
    }

    public void OutputProcessedValues(string input, int input_Length, string input_Uppercase, string input_Replace)
    {
        Console.WriteLine("");
        Console.WriteLine("Input: " + input);
        Console.WriteLine("Uppercase: " + input_Uppercase);
        Console.WriteLine("Length: " + input_Length);
        Console.WriteLine("Replace: " + input_Replace);
    }
    public void ZeroAndAddition(string input_Remove_Zero_CS3, string addition_CS1)
    {
        Console.WriteLine("");
        Console.WriteLine("Remove 0: " + input_Remove_Zero_CS3);
        Console.WriteLine("Addition: " + addition_CS1);
    }
  }
}