import copy

def perm(seq):
  ret = []
  gen(list(seq), 0, ret)
  return ret

def swap(seq, i, j):
  tmp = seq[i]
  seq[i] = seq[j]
  seq[j] = tmp
  

# n is start of seq
def gen(seq, n, results):
  if (n == len(seq)-1):
    results.append(copy.copy(seq))
    return
  for i in xrange(n, len(seq)):
    swap(seq, i, n)
    gen(seq, n+1, results)
    swap(seq, i, n)
    
results = perm('ABC')
for result in results:
  print ''.join(result)
