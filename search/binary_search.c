#include <stdio.h>

#define SIZE 70

int find(int arr[], int value);

int main()
{
    int i = 0;
    int arr[SIZE] = {1, 3, 5, 7, 8, 9, 14, 15, 16, 22, 24, 30, 31, 38, 43, 51, 52, 58, 59, 60, 72, 73, 74, 79, 80, 89, 91, 101, 105, 114, 124, 125, 129, 130, 133, 137, 138, 140, 141, 147, 148, 150, 155, 157, 171, 180, 183, 192, 193, 200, 201, 204, 207, 210, 225, 230, 231, 234, 239, 240, 250, 258, 266, 268, 273, 275, 276, 277, 280, 283};
   
    int values[5] = {7, 283, 203, 140, 56};
    
    for (; i < 5; i++)
    {
        int value = find(arr, values[i]);

        if (value == -1)
        {
            printf("%d not found\n", values[i]);
        }
        else
        {
            printf("%d\n", value);
        }
    }

    return 0;
}

int find(int arr[], int value)
{
    int first = 0;
    int last = SIZE - 1;
    int middle = 0;

    while (first <= last)
    {
        middle = (first + last) / 2;

        if (arr[middle] == value)
        {
            return arr[middle];
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

    return -1;
}

