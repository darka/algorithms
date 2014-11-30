import math

table = [1, 1]

def fib(n):
    while len(table) <= n:
        table.append(table[-1] + table[-2])
    return table[n]
    
def solution(A, B):
    ret = []
    for n, i in enumerate(A):
        ret.append(fib(i) & ((1<<B[n]) - 1))
    return ret