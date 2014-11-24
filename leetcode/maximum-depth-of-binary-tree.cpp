#include <map>
#include <iostream>
#include <stack>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {
public:
    int maxDepth(TreeNode *root) {
        if (!root) return 0;
        stack<TreeNode*> s;
        map<TreeNode*, int> depth;
        s.push(root);
        
        depth[root] = 1;
        int maxDepth = 1;
        TreeNode* maxNode = root;
        
        while (!s.empty()) {
            TreeNode* current = s.top();
            s.pop();
            if (depth[current] >= maxDepth) {
                maxDepth = depth[current];
                maxNode = current;
            }
            if (current->left)
            {
                s.push(current->left);
                depth[current->left] = depth[current] + 1;
            }
            if (current->right)
            {
                s.push(current->right);
                depth[current->right] = depth[current] + 1;
            }
            
        }
        return maxDepth;
    }
};

int main()
{
    TreeNode a(2);
    a.left = NULL;
    a.right = NULL;
    TreeNode b(3);
    b.left = &a;
    b.right = NULL;
    Solution sol;
    cout << sol.maxDepth(&b) <<'\n';
}
