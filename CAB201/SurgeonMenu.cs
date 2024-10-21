using System;

namespace HospitalSystem
{
    public class SurgeonMenu
    {
        private Surgeon surgeon;

        public SurgeonMenu(Surgeon loggedInSurgeon)
        {
            surgeon = loggedInSurgeon;
        }

        public void ShowMenu()
        {
            Console.WriteLine("Surgeon Menu:");
            Console.WriteLine("1. View Schedule");
            Console.WriteLine("2. Perform Surgery");
            Console.Write("Please choose an option: ");
            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    ViewSchedule();
                    break;
                case "2":
                    PerformSurgery();
                    break;
                default:
                    Console.WriteLine("Invalid choice.");
                    break;
            }
        }

        private void ViewSchedule()
        {
            // Simulate viewing surgery schedule
            Console.WriteLine("Viewing surgery schedule...");
        }

        private void PerformSurgery()
        {
            // Simulate performing surgery logic
            Console.WriteLine("Performing surgery...");
        }
    }
}