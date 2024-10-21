namespace HospitalSystem
{
    public class Patient : User
    {
        public int? RoomNumber { get; private set; }

        public Patient(string name, int age, string email, string mobile, string password)
            : base(name, age, email, mobile, password)
        {
        }

        public void CheckIn(int? roomNumber)
        {
            RoomNumber = roomNumber;
        }

        public override string DisplayInfo()
        {
            string baseInfo = base.DisplayInfo();
            return $"{baseInfo}, Room Number: {(RoomNumber.HasValue ? RoomNumber.ToString() : "Not Assigned")}";
        }
    }
}