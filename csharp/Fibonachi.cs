using System;

public static class Fibonachi
{
    public static int Fibo(int n)
    {
        if (n <= 0)
        {
            return 0;
        }
        else if (n == 1)
        {
            return 1;
        }
        else
        {
            return Fibo(n - 1) + Fibo(n - 2);
        }
    }

    public static void Main()
    {
        for (int i = 0; i < 10; i++)
        {
            Console.WriteLine(Fibo(i));
        }
    }
}