#include<stdio.h>

#define SIZE 9

int find(int arr[], int value);

int main()
{
    int i = 0;
    int arr[SIZE] = {1, 3, 5, 7, 9, 11, 14, 21, 28};
    int values[3] = {14, 7, 1};

    for (; i < 3; i++)
    {
        int index = find(arr, values[i]);

        if (index < 0)
        {
            printf("The array is empty");
        }

        printf("The %d is on position %d\n", values[i], index);
    }

    return 0;
}

int find(int arr[], int value)
{
    // if the arr is empty
    if (SIZE < 1)
    {
        return -1;
    }
    
    int first = 0;
    int last = SIZE - 1;
    int middle = -1;

    while (first <= last)
    {
        middle = (first + last) / 2;

        if (arr[middle] == value)
        {
            return middle;
        }
        else
        {
            if (arr[middle] > value)
            {
                last = middle - 1;
            }
            else
            {
                first = middle + 1;
            }
        }
    }
}

