def distance(a, b):
  """Recursively calculate the Levenshtein edit distance between two strings, a and b.
  Returns the edit distance.
  """
  if("" == a): 
      return len(b)   # returns if a is an empty string
  if("" == b): 
      return len(a)   # returns if b is an empty string
  return min(lev(a[:-1], b[:-1])+(a[-1] != b[-1]), lev(a[:-1], b)+1, lev(a, b[:-1])+1)  # Note: True=1 and False=0 when adding a boolean to an integer
