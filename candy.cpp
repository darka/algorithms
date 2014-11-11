#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
class Solution {
public:
    int candy(vector<int> &ratings) {
      if (ratings.size() == 0) return 0;
      vector<int> assignments;
      assignments.push_back(1);
      for (size_t i = 1; i < ratings.size(); ++i)
      {
        int n;
        if (ratings[i] > ratings[i-1])
        {
          n = assignments[i-1]+1;
        }
        else
        {
          n = 1;
        }
        assignments.push_back(n);
      }
      for (size_t i = 0; i < assignments.size(); ++i)
        cout << assignments[i] << ' ';
      cout << '\n';
      for (size_t i = ratings.size()-1; i != 0; --i)
      {
        if (ratings[i-1] > ratings[i] && assignments[i-1] <= assignments[i])
        {
          assignments[i-1] = assignments[i] + 1;
        }
      }
      for (size_t i = 0; i < assignments.size(); ++i)
        cout << assignments[i] << ' ';
      cout << '\n';
      return accumulate(assignments.begin(), assignments.end(), 0);
    }
};


int main()
{
  Solution sol;
  //vector<int> ratings({5,9,2,6,1,7,3,1,9});
  vector<int> ratings({5, 2, 1, 9, 12, 1, 4, 9, 2});
  cout << sol.candy(ratings) << '\n';
}
