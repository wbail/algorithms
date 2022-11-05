#include <stdio.h>
#include <stdlib.h>

#define SIZE 8

struct node
{
	int data;
	struct node* left;
	struct node* right;
};

struct node* root;

void insert(int value);
void in_order(struct node *root);
void search(int value);

int main()
{
    int arr[SIZE] = {3, 5, 1, 2, 7, 6, 10, 11};
    int i = 0;
    
    for (; i < SIZE; i++)
    {
        insert(arr[i]);
    }

    printf("\nShow tree in In Order: ");
    in_order(root);

    printf("\n");

    printf("\nLooking for the value 7:");
    search(7);

    printf("\n");

    printf("\nLooking for the value 11:");
    search(11);

    printf("\n");

    printf("\nLooking for the value 23:");
    search(23);

    printf("\n");

	return 0;
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

void in_order(struct node *root)
{
    if (root != NULL)
    {
        in_order(root->left);

        printf("%d ", root->data);

        in_order(root->right);
    }
}

void search(int value)
{
    struct node *current = root;

    while (current != NULL)
    {
        if (current->data == value)
        {
            printf(" Found!\n");
            return;
        }
        
        if (value < current->data)
        {
            current = current->left;
        }
        else
        {
            current = current->right;
        }
    }

    printf(" Not found!");
}



