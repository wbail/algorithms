//link:https://leetcode.com/problems/count-complete-tree-nodes/
//id:222

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int countNodes(struct TreeNode* root){

    if (root == NULL)
    {
        return 0;
    }
    else
    {
        int leftNodes = countNodes(root->left);

        int rightNodes = countNodes(root->right);

        return leftNodes + rightNodes + 1;
    }
}