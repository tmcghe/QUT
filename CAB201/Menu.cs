using System;

namespace HospitalSystem
{
    public class Menu
    {
        private UserManager userManager = new UserManager();
        private User? loggedInUser = null;
        private IInputValidator inputValidator;
        public Menu(IInputValidator inputValidator)
        {
            this.inputValidator = inputValidator;
        }

        public void Run()
        {
            Console.WriteLine("=================================");
            Console.WriteLine("Welcome to Gardens Point Hospital");
            Console.WriteLine("=================================");
            while (true)
            {
                Console.WriteLine();
                Console.WriteLine("Please choose from the menu below:");
                Console.WriteLine("1. Login as a registered user");
                Console.WriteLine("2. Register as a new user");
                Console.WriteLine("3. Exit");
                Console.Write("Please enter a choice between 1 and 3.");

                string choice = Console.ReadLine();

                if (choice == "1")
                {
                    Login();
                }
                else if (choice == "2")
                {
                    RegisterUser();
                }
                else if (choice == "3")
                {
                    Console.WriteLine(); 
                    Console.WriteLine("Goodbye. Please stay safe.");
                    break;
                }
                else
                {
                    Console.WriteLine("Invalid choice. Please try again.");
                }
            }
        }

        private void RegisterUser()
        {
            Console.WriteLine();
            Console.WriteLine("Register as which type of user:");
            Console.WriteLine("1. Patient");
            Console.WriteLine("2. Staff");
            Console.WriteLine("3. Return to the first menu");
            Console.WriteLine("Please enter a choice between 1 and 3: "); 

            string userType = Console.ReadLine();

            if (userType == "1")
            {
                // Register as a patient
                RegisterPatient();
                Console.WriteLine(); 
            }
            else if (userType == "2")
            {
                // Register as a staff
                RegisterStaff();  
            }
            else if (userType == "3")
            {
                
                Console.WriteLine();  
                return;
            }
            else
            {
                Console.WriteLine("Invalid choice. Please try again.");
                RegisterUser();  
            }
        }

        private void RegisterPatient()
        {
            Console.WriteLine();
            Console.WriteLine("Registering as a patient.");
            string name = inputValidator.GetValidStringInput("Please enter in your name: ");  
            int age = inputValidator.GetValidIntInput("Please enter in your age: ");
            string mobile = inputValidator.GetValidStringInput("Please enter in your mobile number: ");
            string email = inputValidator.GetValidStringInput("Please enter in your email: ");
            string password = inputValidator.GetValidStringInput("Please enter in your password: ");

           
            userManager.RegisterPatient(name, age, email, mobile, password);
            Console.WriteLine($"{name} is registered as a patient.");
        }

private void RegisterStaff()
{
    
    Console.WriteLine("Register as which type of staff:");
    Console.WriteLine("1. Floor manager");
    Console.WriteLine("2. Surgeon");
    Console.WriteLine("3. Return to the first menu");
    Console.Write("Please enter a choice between 1 and 3.");
    Console.WriteLine();

    string staffType = Console.ReadLine();
    if (staffType == "3")
    {
        Console.WriteLine();
        return;
    }
    if (staffType == "1")
    {
        Console.WriteLine("Registering as a floor manager.");
        string name = inputValidator.GetValidStringInput("Please enter in your name: ");
        int age = inputValidator.GetValidIntInput("Please enter in your age: ");
        Console.WriteLine();
        string mobile = inputValidator.GetValidStringInput("Please enter in your mobile number: ");
        string email = inputValidator.GetValidStringInput("Please enter in your email: ");
        string password = inputValidator.GetValidStringInput("Please enter in your password: ");
        int staffId = inputValidator.GetValidIntInput("Please enter in your staff ID: ");
        int floorNumber = inputValidator.GetValidIntInput("Please enter in the floor number you manage: "); ;

        userManager.RegisterFloorManager(name, age, email, mobile, password, staffId, floorNumber);
        Console.WriteLine($"{name} is registered as a floor manager.");
    }
    else if (staffType == "2")
    {
        
        int staffId = inputValidator.GetValidIntInput("Please enter your staff ID: ");
        Console.WriteLine("Select your specialty:");
        Console.WriteLine("1. General Surgeon");
        Console.WriteLine("2. Orthopaedic Surgeon");
        Console.WriteLine("3. Cardiothoracic Surgeon");
        Console.WriteLine("4. Neurosurgeon");
        int specialtyChoice = inputValidator.GetValidIntInput("Please enter a choice between 1 and 4: ");
        string specialty = specialtyChoice switch
        {
            1 => "General Surgeon",
            2 => "Orthopaedic Surgeon",
            3 => "Cardiothoracic Surgeon",
            4 => "Neurosurgeon",
            _ => "Unknown"
        };

        string name = inputValidator.GetValidStringInput("Please enter in your name: ");
        int age = inputValidator.GetValidIntInput("Please enter in your age: ");
        string mobile = inputValidator.GetValidStringInput("Please enter your mobile number: ");
        string email = inputValidator.GetValidStringInput("Please enter your email: ");
        string password = inputValidator.GetValidStringInput("Please enter your password: ");

        userManager.RegisterSurgeon(name, age, email, mobile, password, staffId, specialty);
        Console.WriteLine($"{name} is registered as a {specialty}.");
    }
    else
    {
        // Handle invalid input
        Console.WriteLine("Invalid choice. Please try again.");
        RegisterStaff();  // Prompt the user again
    }
}


        private void Login()
        {
            string email = inputValidator.GetValidStringInput("Enter your email: ");
            string password = inputValidator.GetValidStringInput("Enter your password: ");

            loggedInUser = userManager.Login(email, password);

            if (loggedInUser != null)
            {
                Console.WriteLine($"Login successful! Welcome, {loggedInUser.Name}.");
                LoggedInMenu();
            }
            else
            {
                Console.WriteLine("Invalid email or password. Please try again.");
            }
        }

        private void LoggedInMenu()
        {
            if (loggedInUser is Patient)
            {
                PatientMenu patientMenu = new PatientMenu((Patient)loggedInUser);
                patientMenu.ShowMenu();
            }
            else if (loggedInUser is FloorManager)
            {
                FloorManagerMenu floorManagerMenu = new FloorManagerMenu((FloorManager)loggedInUser);
                floorManagerMenu.ShowMenu();
            }
            else if (loggedInUser is Surgeon)
            {
                SurgeonMenu surgeonMenu = new SurgeonMenu((Surgeon)loggedInUser);
                surgeonMenu.ShowMenu();
            }

            // Option to log out
            Console.WriteLine("1. Logout");
            Console.Write("Please choose an option: ");  // Fix 
            string choice = Console.ReadLine();
            if (choice == "1")
            {
                loggedInUser = null;
                Console.WriteLine("You have been logged out.");
            }
        }
    }
}
