def count_fibonacci(until):
  a = [0, 1]
  sum = 0
  while a[-1] < until:
    a.append(a[-1] + a[-2])
    if a[-1] % 2 == 0:
      sum += a[-1]
  return sum

print count_fibonacci(4000000)
