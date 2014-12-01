class Solution {
public:
    int maxProduct(int A[], int n) {
      
        int currentMax = A[0];
        int currentMin = A[0];
        int ret = A[0];

        for (int i = 1; i < n; i++) {
            int newMax = currentMax * A[i];
            int newMin = currentMin * A[i];
            currentMax = max(A[i], max(newMax, newMin));
            currentMin = min(A[i], min(newMax, newMin));
            ret = max(currentMax, ret);
        }
  
        return ret;
    }
};

