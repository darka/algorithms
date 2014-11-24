#include <iostream>

int main()
{
  short int* a = new short int(511);
  unsigned char* b = (unsigned char*)a;
  std::cout << (int)(b[0]) << ' ' << (int)(b[1]) << '\n';
  delete a;
}
