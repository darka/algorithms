class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while j >= 0 and i >= 0:
            if A[i] > B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1
            k -= 1
            
        # Out of elements in original A, so merge the rest of B
        while j >= 0:
            A[k] = B[j]
            k -= 1
            j -= 1
