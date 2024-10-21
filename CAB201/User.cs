namespace HospitalSystem
{
    public abstract class User
    {
        public string Name { get; private set; }
        public int Age { get; private set; }
        public string Email { get; private set; }
        public string Mobile { get; private set; }
        public string Password { get; private set; }

        public User(string name, int age, string email, string mobile, string password)
        {
            Name = name;
            Age = age;
            Email = email;
            Mobile = mobile;
            Password = password;
        }

        public virtual string DisplayInfo()
        {
            return $"Name: {Name}, Age: {Age}, Email: {Email}, Mobile: {Mobile}";
        }
    }
}