using System;
using Chip;

namespace String_manipulator {

public class Overload {
    public string Value { get; set; }
    public Overload(string value) {
        Value = value;
    }
    public static Overload operator -(Overload s, string toRemove) {
        return new Overload(s.Value.Replace(toRemove, ""));
    }
    public static Overload operator +(Overload left, Overload right) {
        return new Overload(left.Value + right.Value);
    }
}

public class Processing {
    public Processing() {}

    public Processing(string inputCS2, string oldletterCS2, string newletterCS2, string inputCS3, string oldletterCS3, string newletterCS3) 
    {
        Manipulator(inputCS2, oldletterCS2, newletterCS2, inputCS3, oldletterCS3, newletterCS3);
    }
    public Processing(Processing other) {}

    ~Processing() {}

    public void Manipulator(string inputCS2, string oldletterCS2, string newletterCS2, string inputCS3, string oldletterCS3, string newletterCS3)  
    {
        string input_Uppercase_CS2 = inputCS2.ToUpper();
        int input_Length_CS2 = inputCS2.Length;
        string input_Replace_CS2 = inputCS2.Replace(oldletterCS2, newletterCS2);

        string input_Uppercase_CS3 = inputCS3.ToUpper();
        int input_Length_CS3 = inputCS3.Length;
        string input_Replace_CS3 = inputCS3.Replace(oldletterCS3, newletterCS3);

        Overload input_Remove_Zero_CS3 = new Overload(inputCS3) - "0";
        Overload addition_CS1 = new Overload(inputCS2) + new Overload(inputCS3);

        Program transfer = new Program();
        transfer.OutputProcessedValues(inputCS2, input_Length_CS2, input_Uppercase_CS2, input_Replace_CS2);
        transfer.OutputProcessedValues(inputCS3, input_Length_CS3, input_Uppercase_CS3, input_Replace_CS3);

        transfer.ZeroAndAddition(input_Remove_Zero_CS3.Value, addition_CS1.Value);

    }
  }
}