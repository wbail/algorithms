#include<stdio.h>

#define SIZE 9

typedef struct node
{
    int data;
    struct node *left;
    struct node *right;
} node;

struct node *root;

void insert(int value);
int count_nodes(struct node *root);

int main()
{

    int arr[SIZE] = {3, 5, 1, 7, 2, 6, 9, 4, 8};
    int i = 0;

    for (; i < SIZE; i++)
    {
        insert(arr[i]);
    }

    int nodes = count_nodes(root);

    printf("The tree has %d node(s)", nodes);

    return 0;
}

int count_nodes(struct node *root)
{
    if (root == NULL)
    {
        return 0;
    }
    else
    {        
        int leftNodes = count_nodes(root->left);
      
        int rightNodes = count_nodes(root->right);

        return leftNodes + rightNodes + 1;
    }
}

void insert(int value)
{
    struct node *current;
    struct node *aux;

    current = root;

    aux = (node*) malloc(sizeof(node));
    aux->data = value;
    aux->left = NULL;
    aux->right = NULL;

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
