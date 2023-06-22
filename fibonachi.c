#include <stdio.h>


/*

Time complexity of the function printNTermsOfFibonachiSeries(int n) is O(2^n)

*/

int printNTermsOfFibonachiSeries(int n)
{
    if (n <= 0)
        return 0;
    else if (n == 1)
        return 1;
    else
        return printNTermsOfFibonachiSeries(n - 2) + printNTermsOfFibonachiSeries(n - 1);
}

int main ()
{
    int i = 0;
    int n = 10;

    for (i = 1; i <= n; i++)
    {
        printf("%d\n", printNTermsOfFibonachiSeries(i));
    }

    return 0;
}
