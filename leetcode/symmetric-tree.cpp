#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
  bool isSymmetric(TreeNode *root) {
    if (!root) return true;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty())
    {
      std::vector<TreeNode*> checker;
      while (!q.empty())
      {
        checker.push_back(q.front());
        q.pop();
      }
      size_t j = checker.size()-1;
      for (size_t i = 0; i != checker.size(); ++i)
      {
        j = checker.size()-1-i;
        if (i < j) {
          if (checker[i] == 0 && checker[j] == 0) continue;
          if (checker[i] == 0 && checker[j] != 0) return false;
          if (checker[j] == 0 && checker[i] != 0) return false;
          if (checker[i]->val != checker[j]->val) return false;
        }
      }
      bool nonzero = false;
      for (size_t i = 0; i != checker.size(); ++i)
      {
        if (checker[i]) {
          nonzero = true;
          q.push(checker[i]->left);
          q.push(checker[i]->right);
        }
      }
      if (!nonzero) return true;
    }
  }
};

int main()
{
  Solution sol;
  TreeNode root(1);
  TreeNode a(2);
  TreeNode b(2);
  TreeNode c(4);
  TreeNode d(4);
  root.left = &a;
  root.right = &b;
  a.right = &c;
  b.left = &d;
  cout << sol.isSymmetric(&root) << '\n';
}
