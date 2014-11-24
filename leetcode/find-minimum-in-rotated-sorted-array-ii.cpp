#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
  int findMin(vector<int> &num) {
    if (num.size() == 0)
      return 0;
    return findMin(num, 0, num.size());
  }

  int findMin(vector<int> &num, size_t a, size_t b) {
    if (a == b-1 || num[a] < num[b-1])
    {
      return num[a];
    }
    else
    {
      return min(findMin(num, a + (b - a) / 2, b),
                 findMin(num, a, a + (b - a) / 2));
    }
  }
};

int main()
{
  Solution sol;
  vector<int> v({5,5,5,6,6,8,1,2,2});
  cout << sol.findMin(v) << '\n';
}
