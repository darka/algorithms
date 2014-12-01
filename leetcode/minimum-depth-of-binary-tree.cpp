/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int minDepth(TreeNode *root) {
        if (!root) 
            return 0;
            
        stack<TreeNode*> s;
        map<TreeNode*, int> depth;
        s.push(root);
        
        depth[root] = 1;
        int minDepth = numeric_limits<int>::max();

        while (!s.empty()) {
            TreeNode* current = s.top();
            s.pop();
            int children = 0;

            if (current->left)
            {
                s.push(current->left);
                depth[current->left] = depth[current] + 1;
                children++;
            }
            if (current->right)
            {
                s.push(current->right);
                depth[current->right] = depth[current] + 1;
                children++;
            }
            if (children == 0 && depth[current] < minDepth) {
                minDepth = depth[current];
            }
        }
        return minDepth;
    }
};
