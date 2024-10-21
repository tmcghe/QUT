using System;
using System.Collections.Generic;

namespace HospitalSystem
{
    public class UserManager
    {
        private List<User> registeredUsers = new List<User>();

        // Method to register a patient
        public void RegisterPatient(string name, int age, string email, string mobile, string password)
        {
            Patient newPatient = new Patient(name, age, email, mobile, password);
            registeredUsers.Add(newPatient);
        }

        // Method to register a floor manager
        public void RegisterFloorManager(string name, int age, string email, string mobile, string password, int staffId, int floorNumber)
        {
            FloorManager newFloorManager = new FloorManager(name, age, email, mobile, password, staffId, floorNumber);
            registeredUsers.Add(newFloorManager);
        }

        // Method to register a surgeon
        public void RegisterSurgeon(string name, int age, string email, string mobile, string password, int staffId, string specialty)
        {
            Surgeon newSurgeon = new Surgeon(name, age, email, mobile, password, staffId, specialty);
            registeredUsers.Add(newSurgeon);
        }

        // New overloaded Login method with email and password parameters
        public User? Login(string email, string password)
        {
            // If no users are registered, return null immediately
            if (registeredUsers.Count == 0)
            {
                Console.WriteLine("No users are registered in the system. Please register before logging in.");
                return null;
            }

            // Ensure email and password are not null or empty
            if (string.IsNullOrEmpty(email) || string.IsNullOrEmpty(password))
            {
                Console.WriteLine("Email and password cannot be empty.");
                return null;
            }

            // Search for the user in the registeredUsers list
            User? user = registeredUsers.Find(u => u.Email.Equals(email, StringComparison.OrdinalIgnoreCase) && u.Password == password);

            if (user != null)
            {
                Console.WriteLine($"Login successful! Welcome, {user.Name}.");
                return user;
            }
            else
            {
                Console.WriteLine("Invalid email or password. Please try again.");
                return null;
            }
        }

        // Original Login method for backwards compatibility (without parameters)
        public User? Login()
        {
            string? email;
            string? password;

            do
            {
                // Request email input and validate it's not null or empty
                Console.Write("Enter your email: ");
                email = Console.ReadLine();

                if (string.IsNullOrEmpty(email))
                {
                    Console.WriteLine("Email cannot be empty. Please try again.");
                    continue; // Ask for input again
                }
            } while (email == null);

            do
            {
                // Request password input and validate it's not null or empty
                Console.Write("Enter your password: ");
                password = Console.ReadLine();

                if (string.IsNullOrEmpty(password))
                {
                    Console.WriteLine("Password cannot be empty. Please try again.");
                    continue; // Ask for input again
                }
            } while (password == null);

            // Search for the user in the registeredUsers list
            User? user = registeredUsers.Find(u => u.Email.Equals(email, StringComparison.OrdinalIgnoreCase) && u.Password == password);

            if (user != null)
            {
                Console.WriteLine($"Login successful! Welcome, {user.Name}.");
                return user;
            }
            else
            {
                Console.WriteLine("Invalid email or password. Please try again.");
                return null;
            }
        }

        // Optional email format validation
        private bool IsValidEmail(string email)
        {
            // Simple email format validation using System.ComponentModel.DataAnnotations
            try
            {
                var addr = new System.Net.Mail.MailAddress(email);
                return addr.Address == email;
            }
            catch
            {
                return false;
            }
        }

        // Method to display all registered users (for debugging or info purposes)
        public void DisplayAllUsers()
        {
            if (registeredUsers.Count == 0)
            {
                Console.WriteLine("No users are registered in the system.");
            }
            else
            {
                Console.WriteLine("Registered Users:");
                foreach (var user in registeredUsers)
                {
                    Console.WriteLine(user.DisplayInfo());
                }
            }
        }

        // Method to find a user by email (optional utility method)
        public User? FindUserByEmail(string email)
        {
            return registeredUsers.Find(u => u.Email.Equals(email, StringComparison.OrdinalIgnoreCase));
        }
    }
}
