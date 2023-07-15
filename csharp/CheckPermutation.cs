using System;

public class CheckPermutation
{
    public static bool IsPermutation(string str1, string str2)
    {
        int str1Lenght = str1.Length;
        int str2Lenght = str2.Length;

        if (str1Lenght != str2Lenght || string.IsNullOrEmpty(str1) || string.IsNullOrEmpty(str2))
        {
            return false;
        }
		
		char[] str1chars = str1.ToCharArray();
		char[] str2chars = str2.ToCharArray();

        Array.Sort(str1chars);
        Array.Sort(str2chars);

        for (int i = 0; i < str1Lenght; i++)
        {
            if (str1chars[i] != str2chars[i])
            {
                return false;
            }
        }

        return true;
    }

    public static void Main()
    {
        string str1 = "abcd";
        string str2 = "cdba";

        bool result = IsPermutation(str1, str2);

        Console.WriteLine("Is Permutation: " + result);
    }
}