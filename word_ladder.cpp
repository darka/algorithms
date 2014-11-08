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
  int ladderLength(string start, string end, unordered_set<string> &dict) {
    dict.insert(start);
    dict.insert(end);
    unordered_map<string, vector<const string*>> patterns;
    patterns.max_load_factor(0.1);
    for (auto i = dict.begin(); i != dict.end(); ++i)
    {
      auto str = *i;
      for (int j = 0; j < str.size(); ++j)
      {
        char tmp = str[j];
        str[j] = '_';
        patterns[str].push_back(&(*i));
        str[j] = tmp;
      }
    }

    map< const string*, vector< const string* > > arr;
   
    for (auto i = patterns.begin(); i != patterns.end(); ++i)
    {
      //cout << i->first << '\n';
      for (auto j = i->second.begin(); j != i->second.end(); ++j)
      {
        //cout << "  " << (*(*j)) << '\n';
        for (auto k = j+1; k != i->second.end(); ++k)
        {
          arr[(*j)].push_back((*k));
          arr[(*k)].push_back((*j));
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
