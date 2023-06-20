#include <stdio.h>
#include <math.h>

#define SIZE 20

/*

Time complexity of isPrime function is O(sqrt(n))

*/

int isPrime(int n)
{
    int i;

    if (n == 1)
    {
        return 0;
    }
    
    printf("\nNumber: %d", n);
    printf("\nSquare root of %d: %f", n, sqrt(n));

    for (i = 2; i <= sqrt(n); i++)
    {
        printf("\n%d modulus %d = %d", n, i, n % i);
        if (n % i == 0)
        {
            printf("\nThe number %d is NOT prime", n);
            printf("\n------------------------------\n");
            return 0;
        }
    }
    
    printf("\nThe number %d is prime", n);

    printf("\n------------------------------\n");

    return n;
}

void getPrimeNumbersList(int *buf, int count)
{
    for(int i = 0; i < count; ++i)
    {
        buf[i] = isPrime(buf[i]);
        // printf("%d ", buf[i]);
    }
}

int main()
{
    int arr[] = {1,2,3,4,5,6,7,8,9,13,14,15,19,21,25,35,77,91,101,733};

    int i = 0;

    printf("Numbers list: ");

    for (i = 0; i < SIZE; i++)
    {
        printf("%d ", arr[i]);
    }

    printf("\nPrime numbers list: ");

    getPrimeNumbersList(arr, SIZE);

    return 0;
}
