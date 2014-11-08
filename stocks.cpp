#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
  int maxProfit(vector<int> &prices) {
    if (prices.size() == 0)
      return 0;
    int min = prices[0];
    int maxDiff = 0;
    for (size_t i = 1; i < prices.size(); ++i)
    {
      if (prices[i] < min)
      {
        min = prices[i];
      }
      int diff = prices[i] - min;
      if (diff > maxDiff)
      {
        maxDiff = prices[i] - min;
      }
    }
    return maxDiff;
  }
};

int main()
{
  Solution sol;
  vector<int> prices({1,2,3,11, 4, 7});
  cout << sol.maxProfit(prices) << '\n';

}
