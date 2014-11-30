int solution(vector<int> &A) {
    
    if (A.empty()) return 1;

    // Initialise Fibonacci data
    vector<int> fib(A.size() + 2, 1);
    for (size_t i = 2; i < fib.size(); ++i) {
        fib[i] = fib[i-1] + fib[i-2];
    }
    
    const int integer_max = 100001;
    
    vector<int> jumps(A.size() + 1, integer_max);
    vector<int> leaves;
    for (size_t i = 0; i < A.size(); ++i) {
        if (A[i] == 1) {
            leaves.push_back(i);
        }
    }
    leaves.push_back(A.size());
        

    for (int leaf : leaves)
    {
        int i = 0;
        while (fib[i] <= leaf+1) {
            if (-1 + fib[i] == leaf) {
                jumps[leaf] = 1;
                break;
            }
            jumps[leaf] = min(jumps[leaf], jumps[leaf - fib[i]] + 1);
            i += 1;
        }

    }
    
    if (jumps.back() == integer_max)
        return -1;
    else
        return jumps.back();
}
