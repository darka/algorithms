class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeDuplicates(self, A):
        k = 0
        duplicates = set()
        for i in xrange(len(A)):
            if A[i] in duplicates:
                pass
            else:
                duplicates.add(A[i])
                A[k] = A[i]
                k += 1
        return k
        
