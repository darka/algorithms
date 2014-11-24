#include <stack>
#include <iostream>

using namespace std;

class Solution {
public:
  int longestValidParentheses(string s) {
    int ret = 0;
    int last_length = 0;
    stack<pair<size_t, size_t>> parens;
    for (size_t i = 0; i < s.size(); ++i) {
      if (s[i] == '(') {
        if (i > 0 && s[i-1] == '(')
          parens.push(make_pair(i, 0));
        else
          parens.push(make_pair(i, last_length));
      } else if (s[i] == ')') {
        if (parens.empty()) {
          last_length = 0;
          continue;
        }
        auto top = parens.top();
        last_length = top.second + i - top.first + 1;
        if (ret < last_length)
          ret = last_length;
        parens.pop();
      }
    }
    return ret;
  }
};

int main()
{
  Solution sol;
  cout << sol.longestValidParentheses("((()))()") << '\n';
  cout << sol.longestValidParentheses("((()))") << '\n';
  cout << sol.longestValidParentheses("()()()") << '\n';
  cout << sol.longestValidParentheses("((()))(())") << '\n';
  cout << sol.longestValidParentheses("((()))())") << '\n';
  cout << sol.longestValidParentheses("(()()") << '\n';
  cout << sol.longestValidParentheses("()(()") << '\n';
}
