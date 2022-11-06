#include <stdio.h>

#define SIZE 7

struct node
{
    int data;
    struct node* left = NULL;
    struct node* right = NULL;
};

struct node* root;

void insert(int value);
void in_order(struct node* root);
void show_odd_numbers(struct node* root);
void show_even_numbers(struct node* root);

int main()
{
    int arr[SIZE] = {3, 5, 1, 7, 2, 9, 4};

    int i = 0;

    for (; i < SIZE; i++)
    {
        insert(arr[i]);
    }

    printf("\nTree In Order: ");
    in_order(root);

    printf("\nShow Odd numbers: ");
    show_odd_numbers(root);

    printf("\nShow Even numbers: ");
    show_even_numbers(root);

    printf("\n\n");

    return 0;
}

void show_odd_numbers(struct node* root)
{
    if (root != NULL)
    {
        show_odd_numbers(root->left);

        if (root->data % 2 != 0)
        {
            printf(" %d", root->data);
        }

        show_odd_numbers(root->right);
    }
}

void show_even_numbers(struct node* root)
{
    if (root != NULL)
    {
        show_even_numbers(root->left);

        if (root->data % 2 == 0)
        {
            printf(" %d", root->data);
        }
        
        show_even_numbers(root->right);
    }
}

void in_order(struct node* root)
{
    if (root != NULL)
    {
        in_order(root->left);

        printf(" %d", root->data);

        in_order(root->right);
    }
}

void insert(int value)
{
    struct node* current;
    struct node* aux;

    aux = new(struct node);
    aux->data = value;

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

            current = current->left;
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

