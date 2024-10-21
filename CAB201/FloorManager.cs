namespace HospitalSystem
{
    public class FloorManager : User
    {
        public int StaffId { get; private set; }
        public int FloorNumber { get; private set; }

        public FloorManager(string name, int age, string email, string mobile, string password, int staffId, int floorNumber)
            : base(name, age, email, mobile, password)
        {
            StaffId = staffId;
            FloorNumber = floorNumber;
        }

        public override string DisplayInfo()
        {
            string baseInfo = base.DisplayInfo();
            return $"{baseInfo}, Staff ID: {StaffId}, Floor Number: {FloorNumber}";
        }

        public void AssignRoom(Patient patient, int roomNumber)
        {
            patient.CheckIn(roomNumber);
        }
    }
}