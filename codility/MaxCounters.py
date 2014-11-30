vector<int> solution(int N, vector<int> &A) {
    vector<int> ret(N, 0);
    int currentMax = 0;
    int totalMax = 0;
    
    for (int i : A) {
        
        if (i == N + 1) {
            currentMax = totalMax;
            continue;
        }
        
        if (ret[i-1] < currentMax) {
            ret[i-1] = currentMax + 1;
        } else {
            ret[i-1] += 1;
        }
        
        if (ret[i-1] > totalMax) {
            totalMax = ret[i-1];
        }
    }
    
    for (int i = 0; i < N; ++i)
    {
        if (ret[i] < currentMax) 
            ret[i] = currentMax;
    }
    return ret;
}