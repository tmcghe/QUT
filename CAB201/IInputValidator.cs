namespace HospitalSystem
{
    public interface IInputValidator
    {
        string GetValidStringInput(string prompt);
        int GetValidIntInput(string prompt);
    }
}