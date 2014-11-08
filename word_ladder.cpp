#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <queue>

using namespace std;

class Solution {
public:
  int editDistance(string const& a, string const& b) const
  {
    int ret = 0;
    for (size_t i = 0; i < a.size(); ++i)
    {
      if (a[i] != b[i])
        ret++;
    }
    return ret;
  }

  int ladderLength(string start, string end, unordered_set<string> &dict) {
    map< const string*, vector< const string* > > arr;
    dict.insert(start);
    dict.insert(end);

    for (unordered_set<string>::iterator i = dict.begin(); i != dict.end(); ++i)
    {
      unordered_set<string>::iterator j(i);
      for (j++; j != dict.end(); ++j)
      {
        if (editDistance(*i, *j) == 1)
        {
          arr[&(*i)].push_back(&(*j));
          arr[&(*j)].push_back(&(*i));
        }
      }
    }

    queue<pair<const string*, int>> que;

    que.push(make_pair(&(*(dict.find(start))), 1));
    while (!que.empty())
    {
      pair<const string*, int>& current = que.front();
      if ((*current.first) == end)
      {
        return current.second;
      }
      auto& descendants = arr[current.first];
      for (auto i = descendants.begin(); i != descendants.end(); ++i)
      {
        que.push(make_pair(*i, current.second+1));
      }
      que.pop();
    }
    return -1;
  }
};

int main()
{
  Solution sol;
  unordered_set<string> dict({"hot","dot","dog","lot","log"});
  cout << sol.ladderLength("hit", "cog", dict) << '\n';
}
