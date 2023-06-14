#include <stdio.h>

#define SIZE 9

void reverseList(int array[])
{
    int i = 0;

    for (i = 0; i < SIZE / 2; i++)
    {
        int other = (SIZE - i) - 1;
        int temp = array[i];
        array[i] = array[other];
        array[other] = temp;
    }
}

int main ()
{
    int array[SIZE] = {1, 3, 5, 7, 9, 11, 13, 15, 21};
    int i = 0;

    reverseList(array);

    for (i = 0; i < SIZE; i++)
    {
        printf("%d ", array[i]);
    }

    return 0;
}

/*
    Time complexity: O(n)

    Doesn't matter if the array size is divided, for the time complexity
    continues as O(n), where n is the array size  
*/
