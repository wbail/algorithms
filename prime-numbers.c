#include <stdio.h>
#include <math.h>

#define SIZE 9

int isPrime(int n)
{
    if (n == 1)
    {
        return 0;
    }
    
    int aux = sqrt(n) + 1;
    int i;

    for (i = 2; i < aux; i++)
    {
        if (n % i == 0)
        {
            return 0;
        }
    } 

    return n;
}

void getPrimeNumbersList(int *buf, int count)
{
    for(int i = 0; i < count; ++i)
    {
        buf[i] = isPrime(buf[i]);
        printf("%d ", buf[i]);
    }
}

int main()
{
    int arr[] = {1,2,3,4,5,6,7,8,9};

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
