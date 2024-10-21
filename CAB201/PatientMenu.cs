using System;

namespace HospitalSystem
{
    public class PatientMenu
    {
        private Patient patient;

        public PatientMenu(Patient loggedInPatient)
        {
            patient = loggedInPatient;
        }

        public void ShowMenu()
        {
            Console.WriteLine("Patient Menu:");
            Console.WriteLine("1. View Details");
            Console.WriteLine("2. Check in");
            Console.WriteLine("3. Check out");
            Console.Write("Please choose an option: ");
            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    Console.WriteLine(patient.DisplayInfo());
                    break;
                case "2":
                    CheckIn();
                    break;
                case "3":
                    CheckOut();
                    break;
                default:
                    Console.WriteLine("Invalid choice.");
                    break;
            }
        }

        private void CheckIn()
        {
            Console.Write("Enter room number to check in: ");
            int roomNumber = int.Parse(Console.ReadLine());
            patient.CheckIn(roomNumber);
            Console.WriteLine($"Checked in to room {roomNumber}.");
        }

        private void CheckOut()
        {
            if (patient.RoomNumber.HasValue)
            {
                patient.CheckIn(null);  // Nullifying room number to simulate check-out
                Console.WriteLine("Checked out successfully.");
            }
            else
            {
                Console.WriteLine("You are not checked into any room.");
            }
        }
    }
}