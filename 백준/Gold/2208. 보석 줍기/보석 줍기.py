import sys
input = sys.stdin.readline
def solution():
    N, M = map(int, input().split())
    prefix = [0]*(N+1)
    for i in range(1, N+1):
        prefix[i] = prefix[i-1]+int(input())
    res = minVal = 0
    for i in range(M, N+1):
        minVal = min(minVal,prefix[i-M])
        res = max(res,prefix[i]-minVal)
    return res

print(solution())