using System;
using Console_application;

namespace String_manipulator {

public class MainClass {
    public void Main(string input, string oldletter, string newletter)  
    {
        string input_Uppercase = input.ToUpper();
        int input_Length = input.Length;
        string input_Replace = input.Replace(oldletter, newletter);

        Program transfer = new Program();
        transfer.Output(input, input_Length, input_Uppercase, input_Replace);
    }
  }
}   