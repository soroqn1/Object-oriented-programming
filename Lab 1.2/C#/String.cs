using System;
using Chip;

namespace Chip {

public class MainClass {
    private string input;
    private string oldletter;
    private string newletter;

    public MainClass() 
    {
        input = string.Empty;
        oldletter = string.Empty;
        newletter = string.Empty;
    }

    public MainClass(string input, string oldletter, string newletter) 
    {
        this.input = input;
        this.oldletter = oldletter;
        this.newletter = newletter;
        Main(input, oldletter, newletter);
    }

    public MainClass(MainClass other) 
    {
        this.input = other.input;
        this.oldletter = other.oldletter;
        this.newletter = other.newletter;
    }

    ~MainClass() {
    }

    public void Main(string input, string oldletter, string newletter)  
    {
        string input_Uppercase = input.ToUpper();
        int input_Length = input.Length;
        string input_Replace = input.Replace(oldletter, newletter);

        Program transfer = new Program();
        transfer.OutputProcessedValues(input, input_Length, input_Uppercase, input_Replace);
    }
  }
}