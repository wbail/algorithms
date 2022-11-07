#include <stdio.h>

#define SIZE 8

struct node
{
    int data;
    struct node* left;
    struct node* right;
};

struct node* root;

void insert(int value);
void in_order(struct node* root);
int find_tree_height(struct node* root);

int main()
{
    int arr[SIZE] = {3, 5, 1, 7, 2, 6, 9, 4};

    int i = 0;

    for (; i < SIZE; i++)
    {
        insert(arr[i]);
    }

    printf("\nTree In Order:");
    in_order(root);

    printf("\n");

    int treeHeight = find_tree_height(root);
    printf("\nTree height: %d", treeHeight);

    printf("\n\n");
    
    return 0;
}

int find_tree_height(struct node* root)
{
    if (root == NULL)
    {
        return 0;
    }
    else
    {
        int leftHeight = find_tree_height(root->left);

        int rightHeight = find_tree_height(root->right);
        
        if (leftHeight >= rightHeight)
        {
            return leftHeight + 1;
        }
        else
        {
            return rightHeight + 1;
        }
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

