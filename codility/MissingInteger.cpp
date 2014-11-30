#include <queue>

void radixSort(vector<int>& A)
{
    
    int j = 1;
    for (size_t n = 1; n < 10; ++n)
    {
        vector<queue<int>> buckets(10);
        for (int i : A) {
            buckets[i / j % 10].push(i);
        }
        int k = 0;
        
        // Empty all the buckets into array
        for (queue<int>& q : buckets)
        {
            while (!q.empty())
            {
                A[k] = q.front();
                q.pop();
                k++;
            }
        }
        j *= 10;
    }
}

int solution(vector<int> &A) {
    vector<int> B; // Only positive integers from A
    
    for (int i : A) {
        if (i > 0)
            B.push_back(i);
    }
    
    if (B.empty()) return 1;
    
    radixSort(B);
    
    if (B[0] != 1) return 1; // all integers in B larger than 1
    
    for (size_t i = 0; i < B.size() - 1; ++i) {
        if (B[i+1] - B[i] > 1)
            return B[i] + 1;
    }
    return B.back() + 1;
}