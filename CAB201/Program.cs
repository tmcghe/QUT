using System;

namespace HospitalSystem
{
    class Program
    {
        static void Main(string[] args)
        {
            IInputValidator inputValidator = new InputValidator();
            Menu menu = new Menu(inputValidator);
            menu.Run();
        }
    }
}