#include <stdio.h>

#define SIZE 5

int hasUniqueChars(char arr[])
{
    int i = 0;
    int j = 0;

    for (i = 0; i < SIZE; i++)
    {
        for (j = 0; j < SIZE; j++)
        {
            if (arr[i] == arr[j] && i != j)
            {
                return 1;
            }
        }
    }

    return 0;
}

int main ()
{
    // char arr[SIZE] = {'a', 'b', 'c', 'd', 'e'}; // False
    char arr[SIZE] = {'a', 'b', 'c', 'a', 'e'}; // True

    int result = hasUniqueChars(arr);

    printf("Result: %d\n", result);

    return 0;
}