class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        k = 0
        for i in xrange(len(A)):
            if elem == A[i]:
                pass
            else:
                A[k] = A[i]
                k += 1
        return k
        
