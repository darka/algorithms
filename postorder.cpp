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
    stack<TreeNode*> s;
    unordered_set<TreeNode*> visited;
    vector<int> postorderTraversal(TreeNode *root) {
        vector<int> ret;
        if (!root) return ret;
        s.push(root);
        
        while (!s.empty())
        {
            TreeNode* top = s.top();
            
            int visited_children = 0;
            
            if (top->right && visited.find(top->right) == visited.end())
                s.push(top->right);
            else
                visited_children++;
            
            if (top->left && visited.find(top->left) == visited.end())
                s.push(top->left);
            else
                visited_children++;
                
            if (visited_children == 2)
            {
                ret.push_back(top->val);
                visited.insert(top);
                s.pop();
            }
        }
    }
};
