#include<stdio.h>

#define SIZE 7

typedef struct Node
{
    int data;
    struct Node *left;
    struct Node *right;
} Node;

struct Node *root;

void insert(int value);
int sum_nodes(struct Node *root);

int main()
{
    int i = 0;
    int sum = 0;
    int arr[SIZE] = {3, 5, 1, 7, 2, 6, 9};

    for (; i < SIZE; i++)
    {
        insert(arr[i]);
    }

    sum = sum_nodes(root);
    printf("\nSum nodes: %d\n", sum);

    return 0;
}

int sum_nodes(struct Node *root)
{
   if (root != NULL)
   {
        int sumLeft = sum_nodes(root->left);

        int sumRight = sum_nodes(root->right); 

        return sumLeft + sumRight + root->data;
   }

   return 0;
}

void insert(int value)
{
    struct Node *current;
    struct Node *aux;

    aux = new(struct Node);
    aux->data = value;
    aux->left = NULL;
    aux->right = NULL;

    current = root;

    if (current == NULL)
    {
        root = aux;
        return;
    }

    while (1)
    {
        if (value < current->data)
        {
            if (current->left == NULL)
            {
                current->left = aux;
                return;
            }
            else
            {
                current = current->left;
            }
        }
        else if (current->right == NULL)
        {
            current->right = aux;
            return;
        }
        else
        {
            current = current->right;
        }
    }
}
