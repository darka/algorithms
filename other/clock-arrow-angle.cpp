#include <iostream>
#include <cmath>
using namespace std;

double angle(int hour, int minute)
{
  hour = hour % 12;
  double hour_arrow = (double) hour + (double) minute / 60;
  hour_arrow = hour_arrow * 360 / 12.0;
  double minute_arrow = (double) minute * 360 / 60;
  double angle = fabs(hour_arrow - minute_arrow);
  if (angle >= 180)
    angle = 360 - angle;
  return angle;
}

int main()
{
  std::cout << angle(12, 10) << '\n';
  std::cout << angle(20, 50) << '\n';
  std::cout << angle(1, 30) << '\n';
  std::cout << angle(6, 30) << '\n';
  std::cout << angle(6, 0) << '\n';
  std::cout << angle(0, 0) << '\n';
  std::cout << angle(12, 0) << '\n';
}
