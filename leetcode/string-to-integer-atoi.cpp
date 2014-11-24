#include <iostream>
#include <map>
#include <cstring>
#include <cctype>
#include <climits>

using namespace std;

class Solution {
public:
  int atoi(const char *str) {
    int ret = 0;
    int length = strlen(str);
    bool started = false;
    bool neg = false;
    for (size_t i = 0; i < length; ++i)
    {
      char c = str[i];

      if (!started)
      {
        if (isspace(c))
          continue;

        if (c == '+') 
        {
          started = true;
          continue;
        }
  
        if (c == '-')
        {
          started = true;
          neg = true;
          continue;
        }
      }

      int n = (int)c - 48;
      if (0 <= n && n <= 9)
      {
        started = true;
        if ((ret > INT_MAX / 10) ||
            (ret == INT_MAX / 10 && n > INT_MAX % 10))
        {
          if (neg) return INT_MIN;
          else return INT_MAX;
        }
        ret *= 10;
        ret += n;
      }
      else
      {
        break;
      }
    }
    if (neg) ret *= -1;
    return ret;
  }
};


int main()
{
  Solution sol;
  std::cout << sol.atoi("123") << '\n';
  std::cout << sol.atoi("     123") << '\n';
  std::cout << sol.atoi("    \n 123.4") << '\n';
  std::cout << sol.atoi("    \n 999999TEST") << '\n';
  std::cout << sol.atoi("    \n 2147483646TEST") << '\n';
}
