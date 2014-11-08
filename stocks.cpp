#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    pair<size_t, size_t> buy_sell(vector<int>& prices, size_t a, size_t b)
    {
        if (b - a > 2)
        {
            pair<size_t, size_t> resultA = buy_sell(prices, a, a + (b - a) / 2);
            pair<size_t, size_t> resultB = buy_sell(prices, a + (b - a) / 2, b);
            int diffA = 0;
            int diffB = 0;
            if (resultA.first < resultA.second)
            {
                diffA = prices[resultA.second] - prices[resultA.first];
            }
            if (resultB.first < resultB.second)
            {
                diffB = prices[resultB.second] - prices[resultB.first];
            }

            int diffC = prices[resultB.second] - prices[resultA.first];

            if (diffC > diffA && diffC > diffB)
            {
                return make_pair(resultA.first, resultB.second);
            }

            if (diffA > diffB)
            {
                return resultA;
            }
            else
            {
                return resultB;
            }
        }
        else if (b - a == 1)
        {
            return make_pair(a, a);
        }
        else
        {
            if (prices[a] < prices[b-1])
            {
                return make_pair(a, b-1);
            }
            else
            {
                return make_pair(b-1, a);
            }
        }
    }
    int maxProfit(vector<int> &prices) {
        if (prices.size() == 0)
        {
            return 0;
        }
        pair<size_t, size_t> result = buy_sell(prices, 0, prices.size());
        if (result.second <= result.first)
        {
            return 0;
        }
        return prices[result.second] - prices[result.first];        
    }

};

int main()
{
    Solution sol;
    vector<int> prices({1,2,3,11, 4, 7});
    cout << sol.maxProfit(prices) << '\n';

}
