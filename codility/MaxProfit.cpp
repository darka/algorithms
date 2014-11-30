def solution(A):
    if len(A) < 2: 
        return 0
        
    buy = 0
    sell = 1
    maxProfit = A[sell] - A[buy]
    
    for i in xrange(1, len(A)):
        if A[i] < A[buy]:
            buy = i
            continue
        
        profit = A[i] - A[buy]
        if profit > maxProfit:
            sell = i
            maxProfit = profit
    
    if maxProfit <= 0:
        return 0
    
    return maxProfit
