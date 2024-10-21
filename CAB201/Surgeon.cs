namespace HospitalSystem
{
    public class Surgeon : User
    {
        public int StaffId { get; private set; }
        public string Specialty { get; private set; }

        public Surgeon(string name, int age, string email, string mobile, string password, int staffId, string specialty)
            : base(name, age, email, mobile, password)
        {
            StaffId = staffId;
            Specialty = specialty;
        }

        public override string DisplayInfo()
        {
            string baseInfo = base.DisplayInfo();
            return $"{baseInfo}, Staff ID: {StaffId}, Specialty: {Specialty}";
        }
    }
}
