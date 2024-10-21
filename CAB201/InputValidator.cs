using System;

namespace HospitalSystem
{
    public class InputValidator : IInputValidator
    {
        public string GetValidStringInput(string prompt)
        {
            string input;
            do
            {
                Console.WriteLine(prompt);
                input = Console.ReadLine();
            } while (string.IsNullOrEmpty(input)); // Ensures the input is not null or empty

            return input;
        }

        public int GetValidIntInput(string prompt)
        {
            int validInt;
            string input;
            do
            {
                Console.WriteLine(prompt);
                input = Console.ReadLine();
            } while (!int.TryParse(input, out validInt)); // Ensures the input is a valid integer

            return validInt;
        }
    }
}