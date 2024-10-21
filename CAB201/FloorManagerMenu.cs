using System;

namespace HospitalSystem
{
    public class FloorManagerMenu
    {
        private FloorManager floorManager;

        public FloorManagerMenu(FloorManager loggedInFloorManager)
        {
            floorManager = loggedInFloorManager;
        }

        public void ShowMenu()
        {
            Console.WriteLine("Floor Manager Menu:");
            Console.WriteLine("1. View Details");
            Console.WriteLine("2. Assign Room to Patient");
            Console.Write("Please choose an option: ");
            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    Console.WriteLine(floorManager.DisplayInfo());
                    break;
                case "2":
                    AssignRoom();
                    break;
                default:
                    Console.WriteLine("Invalid choice.");
                    break;
            }
        }

        private void AssignRoom()
        {
            
            Console.WriteLine("Assigning a room to a patient...");
            //WORK IN PROGRESS
        }
    }
}