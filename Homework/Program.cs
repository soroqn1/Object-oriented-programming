using System;
using System.Collections.Generic;
using System.Linq;

public class TextContainer
{
    private string _text;
    private string[] _lines;
    private int _lineCount;

    public TextContainer(string text)
    {
        Text = text;
    }

    public string Text
    {
        get { return _text; }
        set
        {
            _text = value;
            _lines = _text.Split(new[] { "\r\n", "\r", "\n" }, StringSplitOptions.None);
            _lineCount = _lines.Length;
        }
    }

    public int LineCount
    {
        get { return _lineCount; }
        private set { _lineCount = value; }
    }

    public string this[int index]
    {
        get
        {
            if (index < 0 || index >= _lineCount)
                throw new IndexOutOfRangeException("Індекс виходить за межі тексту");
            
            return _lines[index];
        }
    }

    public void DisplayAllLines()
    {
        for (int i = 0; i < _lineCount; i++)
        {
            Console.WriteLine($"Рядок {i}: {_lines[i]}");
        }
    }
}

// usage
class Program
{
    static void Main()
    {
        TextContainer container = new TextContainer(
            "Перший рядок тексту.\nДругий рядок.\nТретій рядок тексту."
        );
        
        Console.WriteLine($"Кількість рядків: {container.LineCount}");
        
        Console.WriteLine($"Другий рядок: {container[1]}");
        
        container.DisplayAllLines();
        
        container.Text = "Оновлений текст.\nЗ новими рядками.\nІ ще один рядок.";
        Console.WriteLine("\nПісля оновлення тексту:");
        Console.WriteLine($"Нова кількість рядків: {container.LineCount}");
        container.DisplayAllLines();
    }
}